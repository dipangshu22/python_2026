class car:
    def __init__(self,type):
     self.type=type

class toyato(car):
   def __init__(self,type):
      super().__init__(type) #using parent class 




s1=toyato("innova")
print(s1.type)
