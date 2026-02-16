class student:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    
    def avg(self):
        num=0
        for i in self.subject:
         num+=i
        print("hello",self.name,"your average mark is",num/3)
            


s1=student("ravi",[88,56,46])
s1.avg()
s1.name=input("enter name")
s1.avg()