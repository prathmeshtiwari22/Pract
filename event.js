
const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  clientId: "eda-learning-demo",
  brokers: ["localhost:9092"],
});

const TOPIC = "order-events";

// ========================================
// 1. CREATE KAFKA TOPIC
// ========================================

async function ensureTopicExists() {
  const admin = kafka.admin();

  await admin.connect();

  try {
    await admin.createTopics({
      waitForLeaders: true,
      topics: [
        {
          topic: TOPIC,
          numPartitions: 1,
          replicationFactor: 1,
        },
      ],
    });

    console.log(`[Kafka] Topic "${TOPIC}" is ready.`);
  } finally {
    await admin.disconnect();
  }
}

// ========================================
// 2. PRODUCER: PUBLISH AN EVENT
// ========================================

async function publishOrderCreated(order) {
  const producer = kafka.producer();

  await producer.connect();

  try {
    const event = {
      eventId: `evt-${Date.now()}`,
      eventType: "order.created",
      occurredAt: new Date().toISOString(),
      data: order,
    };

    await producer.send({
      topic: TOPIC,
      messages: [
        {
          key: String(order.orderId),
          value: JSON.stringify(event),
        },
      ],
    });

    console.log("\n[Order Service] Event published:");
    console.log(JSON.stringify(event, null, 2));
  } finally {
    await producer.disconnect();
  }
}

// ========================================
// 3. SERVICE FUNCTIONS
// Each service has its own responsibility
// ========================================

async function reserveInventory(order) {
  console.log(
    `[Inventory Service] Reserving ${order.quantity} item(s) ` +
    `for order ${order.orderId}`
  );
}

async function sendOrderConfirmation(order) {
  console.log(
    `[Notification Service] Sending confirmation to ${order.email}`
  );
}

async function createInvoice(order) {
  console.log(
    `[Billing Service] Creating invoice for order ${order.orderId}. ` +
    `Total: Rs.${order.total}`
  );
}

// ========================================
// 4. CONSUMER: LISTEN FOR EVENTS
// ========================================

async function startServiceConsumer({
  serviceName,
  groupId,
  handler,
}) {
  const consumer = kafka.consumer({ groupId });

  await consumer.connect();

  await consumer.subscribe({
    topic: TOPIC,
    fromBeginning: true,
  });

  await consumer.run({
    eachMessage: async ({ message }) => {
      if (!message.value) return;

      try {
        const event = JSON.parse(message.value.toString());

        // Ignore events this service doesn't handle.
        if (event.eventType !== "order.created") {
          return;
        }

        console.log(
          `\n[${serviceName}] Received event: ${event.eventType}`
        );

        await handler(event.data);
      } catch (error) {
        console.error(
          `[${serviceName}] Event processing failed:`,
          error
        );
      }
    },
  });

  console.log(
    `[${serviceName}] Listening to topic "${TOPIC}".`
  );

  return consumer;
}

// ========================================
// 5. APPLICATION ENTRY POINT
// ========================================

async function main() {
  const consumers = [];
  let shuttingDown = false;

  try {
    // Create the topic before starting consumers.
    await ensureTopicExists();

    // Every service has a DIFFERENT consumer group.
    // This allows all services to receive the event.

    consumers.push(
      await startServiceConsumer({
        serviceName: "Inventory Service",
        groupId: "inventory-service",
        handler: reserveInventory,
      })
    );

    consumers.push(
      await startServiceConsumer({
        serviceName: "Notification Service",
        groupId: "notification-service",
        handler: sendOrderConfirmation,
      })
    );

    consumers.push(
      await startServiceConsumer({
        serviceName: "Billing Service",
        groupId: "billing-service",
        handler: createInvoice,
      })
    );

    // Give consumers time to join their groups.
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Simulate a customer placing an order.
    await publishOrderCreated({
      orderId: "ORD-1001",
      product: "Mechanical Keyboard",
      quantity: 1,
      email: "learner@example.com",
      total: 3499,
    });

    console.log(
      "\nEvent published. Press Ctrl+C to stop."
    );
  } catch (error) {
    console.error("\nKafka application failed:", error);
    await shutdown();
    process.exitCode = 1;
  }

  async function shutdown() {
    if (shuttingDown) return;
    shuttingDown = true;

    console.log("\nShutting down Kafka consumers...");

    await Promise.allSettled(
      consumers.map((consumer) => consumer.disconnect())
    );
  }

  process.once("SIGINT", async () => {
    await shutdown();
    process.exit(0);
  });

  process.once("SIGTERM", async () => {
    await shutdown();
    process.exit(0);
  });
}

main();
