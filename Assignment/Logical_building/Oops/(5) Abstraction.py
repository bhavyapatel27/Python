" The method which have only declaration but not a defination (task to do in method) is known as a abstract method "
" & a class which have a abstract method is known as a abstract class"
" We can not create a obj of a abstract class"
" Python doesn's support abstract but we can create a abstract class by importing it "
" import abc import ABC, abstractmethod "
" Abstract meaning in eng: Just thoughts in mind which doesn't have concreate(physical) structure "
" A method that is declared without an implementation, means we can use it for declare a guidelines and etc...."
" 1 abstract method can make a whole class abstract "
" that's why we can't declare a obj in a abstract class, because obj is used to implement a properties of the class!! But abstract is just a imagination "
" By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. "

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class Creditcard(Payment):
    def process_payment_1(self):
        print("Hii, i'm Creditcard")


class Paypal(Payment):
    def process_payment(self):
        print("hii, i'm Paypal")


obj1 = Creditcard()
obj1.process_payment_1()

obj2 = Paypal()
obj2.process_payment()
