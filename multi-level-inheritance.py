class student:
    var1="welcome to saint robert"


class class1(student):
    var2="this is class1"

class class2(class1): #multi-level inheritance
    print ("this is class 2")


s2=class2()
print(s2.var2)
print(s2.var1)