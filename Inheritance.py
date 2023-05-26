class mammal:
    def walk(self):
        print("walk")

class Dog(mammal):
    def bark(self):
        print("bark")
    
class cat(mammal):
    def annoying(self):
        print("annoiyng")
   
dog1=Dog()
dog1.walk()
dog1.bark()
cat1=cat()
cat1.walk()
cat1.annoying()
