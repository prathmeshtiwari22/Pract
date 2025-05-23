#poly method overriding
class Animal:
    def make_sound(self):
        print("HELLO")
class Dog(Animal):
    def make_sound(self):
        print("WOOF WOOF")
        
p1=Dog()
p1.make_sound()
