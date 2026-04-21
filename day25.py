'''
multi-level inhertance
----------------------
--->this occurs when a class inherits from 




class grandparent:
    def show_grandparent(self):
        print("I'm grandparent")

class parent(grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child(self):
        print("I'm child")

any = child()
any.show_grandparent()
any.show_parent()
any.show_child()


HIERCHICAL INHERTANCE
---------------------

---->THIS OCCURS WHEN MULTIPLE CHILD CLASSES INHERIT FROM A SINGLE PARENT
CLASS, THIS PROCESS IS CALLED HIERCHICAL


class parent:
    def parent_(self):
        print("I am parent")

class child_1(parent):
    def child_1(self):
        print("I am 1st child")

class child_2(parent):
    def child_2(self):
        print("I am 2nd child")

class child_3(child_1, child_2):
    def child_3(self):
        print("I am the child")

thing = child_3()
thing.parent_()  #  I am parent
thing.child_1()  #  I am 1st child
thing.child_2()  #  I am 2nd child
thing.child_3()  #  I am the child

HYBRID 
------

class grandparent:
    def show_grandparent(self):
        print("I'm grandparent")

class parent(grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child(self):
        print("I'm child")
class parent:
    def parent_(self):
        print("I am parent")

class child_1(parent):
    def child_1(self):
        print("I am 1st child")

class child_2(parent):
    def child_2(self):
        print("I am 2nd child")

class child_3(child_1, child_2, grandparent):
    def child_3(self):
        print("I am inherited from grandparent class and child_1, child_2")

thing = child_3()
thing.show_grandparent()
thing.parent_()  #  I am parent
thing.child_1()  #  I am 1st child
thing.child_2()  #  I am 2nd child
thing.child_3()  #  I am the child
        
'''
























