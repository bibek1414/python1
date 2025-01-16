# singele inheritaince
# Parent class
class Animal:
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):
    def speak(self):
        return "Dog Barks"
    
my_dog=Dog()
print(my_dog.speak())

# Multiple Inheritance

class A:
    def method_A(self):
        return "A"
class B:
    def method_B(self):
        return "B"
class C(A,B):
    def method_C(self):
        return "C"

obj_c=C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())
# multilelevel
class A:
    def method_A(self):
        return "A"
class B(A):
    def method_B(self):
        return "B"
class C(B):
    def method_C(self):
        return "C"

obj_c=C()
print(obj_c.method_A())
print(obj_c.method_B())
print(obj_c.method_C())
    
        
    