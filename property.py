class marks():
    def __init__(self,math,physics,eng):
        self.math=math
        self.physics=physics
        self.eng=eng
    @property
    def percentage(self):
        return (self.math+self.physics+self.eng)/3
    

s1=marks(22,33,44)
print(s1.math)
print(s1.percentage)
s1.physics=67
print(s1.percentage)
    