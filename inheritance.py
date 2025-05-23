class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal):
    def bark(self):
        print("WOOF WOOF")
        
p1=Dog()
p1.bark()
p1.speak()
