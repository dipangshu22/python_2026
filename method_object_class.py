class car:
    def __init__(self,name,cc):
        print("loading cars list........")
        self.name=name
        self.cc=cc
    def hello(self):
        print("hello object method")

s1=car("bmw",2800)
print(s1.name,s1.cc,s1.hello())
s1.hello()

        