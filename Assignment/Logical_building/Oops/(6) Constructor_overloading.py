" Constructor overriding : 2 constructors in a same class like 2 __init__ methods in a same class "
" and if i write 2 same method in a same class then it will compulsoryly executes 2nd method means 1st method is overrided by 2nd method"
" Python doesn't suports constructor overloading "
" So for that we can take a help of setter and getter "
" And every industry want's we use setter to set the values and getter to get the values "
" we have to do some changes in constructor to achieve properties like constructor overloading "

"Overriding in inheritance:"

# class A:
#     def __init__(self):
#         print("Hy")
#     def __init__(self):
#         print("by")
#
# s1 = A()

"obj will exccute only last constructor"

" "

# class A:
#     def __init__(self):
#         print("Hy")
#
#
# class B(A):
#     def __init__(self):
#         print("By")
#
#
# s1 = B()

"B is inherites from A but as B have it's own Constructor so it's first try to executes it's own constructor"
"So that is known as we have overrided class A constructor in class B"
"That is known as a constructor overriding in inheritance"

"""
NOTE:
IF I CHANGE THE PARAMETERS LIKE I PASS 2 PARAMETRS IN A OBJECT THEN ALSO B'S CONSTRUCTOR IS CALLED
BECAUS THAT IS CALLED AS(PASSING MULTIPLE ARGUMENTS IN A CONSTRUCTOR) IS KNOWN AS A OVERLOADING
&
PYTHON DOESN'T SUPPORTS OVERLOADING
SO MISSING PARAMETERS ARGUMENT WILL SHOW ON terminal
"""

"Heirarchy is object will excecutes firstly the constructor of the class in which it is initiated"

"if object doen's find the constructor of current class then it will move to the super class and executes that constructor"

"Now Requirement is i want to execute 1st super class constructor then i want to execute current class constructor - Use Super"

"Super is method to call constructor of super class in sub class"

# class Person:
#     def __init__(self, age):
#         self.age = age
#         print(age)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name, age)
#
#
# ob_1 = Person(20)

from multipledispatch import dispatch


class Person:
    @dispatch(str, str)
    def product(name, age):
        result = name + age
        print(result)

    # passing two parameters

    @dispatch(str)
    def product(name):
        result = name
        print(result)


ayush = Person.product('2', '5')
bhavya = Person.product('2')
