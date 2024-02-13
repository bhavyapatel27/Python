class A:
    def display(self):
        print("Hey i'm display from the class A")


class B:
    def display(self):
        print("Hey i'm display from the class B")


class C(A, B):
    pass


ob_1 = C()
ob_1.display()

" Conclusion : Execution of method is depends on the order of class which i mentioned in a inherited class(c) "


