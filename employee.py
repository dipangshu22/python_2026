class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        user=input("enter r for role,d for department,s for salary: ")
        if(user=="r"):
            print(self.role)
        elif(user=="d"):
            print(self.department)
            
        else:
            print(self.salary)

class engineer(employee):
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","webdev",80000)

   


# s1=employee("hr","software dev",60000)
# s1.showdetails()


s2=engineer("ravi",29)
s2.showdetails()