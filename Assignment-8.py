# In Python Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
class A:
    def display_A(self):
        print("Display function of base class A")
class B(A):
    def display_B(self):
        print("Display function of derived class B")
b=B()
b.display_A()
b.display_B()
"""
Output of Create 2 classes for single inheritance named respectively A(base class) and B(derived class):
Display function of base class A
Display function of derived class B
"""
# In Python Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor
class A:
    __a=None # Private member a 
    _b=None # Protected member b
    c=None # public member c
    def __init__(self,a,b,c):
        self.__a=a # Private member a
        self._b=b # Protected member b
        self.c=c # public member c
    def display_privatemember(self):
        print("The private member is : ",self.__a)
    def display_protectedmember(self):
        print("The protected member is : ",self._b)
    def display_publicmember(self):
        print("The public member is :",self.c)
a=A(10,20,30)
a.display_privatemember()
a.display_protectedmember()
a.display_publicmember()
"""
Output of In Python Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor
The private member is :  10
The protected member is :  20
The public member is : 30
"""
# In Python Create a method known as display in both the classes, to display the values of a,b and c
class A:
    a=10
    b=20
    c=30
    def display(self):
        print("The value of a is : ",self.a)
        print("The value of b is : ",self.b)
        print("The value of c is : ",self.c)
class B(A):
    a=15
    b=25
    c=35
    def display(self):
        print("The value of a is : ",self.a)
        print("The value of b is : ",self.b)
        print("The value of c is : ",self.c)
a=A()
a.display()
b=B()
b.display()
"""
Output of Create a method known as display in both the classes, to display the values of a,b and c:
The value of a is :  10
The value of b is :  20
The value of c is :  30
The value of a is :  15
The value of b is :  25
The value of c is :  35
"""
# In Python While accessing the private member an exception should be raised and a personalized message should be displayed and the exception should be handled properly so that the rest of the code can get executed
class MyClass:
    _a=None
    def __init__(self,a):
        self._a=a
    def display(self):
        print("a : ",self._a)
    def access_private_member(self):
        try:
            raise AttributeError("Access to private member is not allowed.")
        except AttributeError as e:
            print(str(e))  
obj = MyClass(10)
obj.display()
obj.access_private_member()
"""
Output of While accessing the private member an exception should be raised and a personalized message should be displayed and the exception should be handled properly so that the rest of the code can get executed:
a :  10
Access to private member is not allowed.
"""
"""
Output of entire code is :
Display function of base class A
Display function of derived class B
The private member is :  10
The protected member is :  20
The public member is : 30
The value of a is :  10
The value of b is :  20
The value of c is :  30
The value of a is :  15
The value of b is :  25
The value of c is :  35
a :  10
Access to private member is not allowed.
"""