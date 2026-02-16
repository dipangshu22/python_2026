class student:
    def __init__(self,name):
        self.__name=name #now it is private cannot be accessed outside class,but can be accessed inside a method.

    def hello(self):
        print(self.__name)



s1=student("ravi")



