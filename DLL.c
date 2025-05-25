#include<stdio.h>
#include<stdlib.h>
struct Node{
    int Data;
    struct Node *prev;
    struct Node *next;
};
void traversal(struct Node *ptr){
    while(ptr!=NULL){
       printf(" %d ",ptr->Data); 
       ptr=ptr->next;
    }
    printf("\n ");
}
struct Node *IAS(struct Node* head,int Data){
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->Data=Data;
    head->prev=ptr;
    ptr->next=head;
    return ptr;
}

struct Node *DAI(struct Node* head,int index){
    struct Node* p=head;
    struct Node* q=head->next;
    struct Node* x=head->next->next;
    int i=0;
    while(i!=index-1){
        p=p->next;
        q=q->next;
        x=x->next;
        i++;
    }
    p->next=q->next;
    x->prev=p;
    free(q);
    return head;
}

struct Node *IAI(struct Node* head,int Data,int index){
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->Data=Data;
    struct Node* p=head;
    struct Node* q=head->next;
    int i=0;
    while(i!=index-1){
       p=p->next;
       q=q->next;
       i++;
    }
    ptr->next=p->next;
    ptr->prev=p;
    p->next=ptr;
    q->prev=ptr;
    return head;
}

int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;
    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    fourth=(struct Node*)malloc(sizeof(struct Node));
    head->Data=10;
    head->prev=NULL;
    head->next=second;
    second->Data=20;
    second->prev=head;
    second->next=third;
    third->Data=30;
    third->prev=second;
    third->next=fourth;
    fourth->Data=40;
    fourth->prev=third;
    fourth->next=NULL;
    traversal(head);
    head=IAI(head,7,2);
    traversal(head);
    DAI(head,2);
    traversal(head);
    
    return 0;
}
