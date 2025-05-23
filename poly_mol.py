# method overloading 
class Animal:
    def add(self,a,b,c=0):
        print(a+b+c)
q1=Animal()
q1.add(2,3)
q1.add(2,3,4)
