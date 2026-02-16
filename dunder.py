class operator:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return operator(newreal,newimg)


s1=operator(2,3)
s1.shownumber()

s2=operator(6,9)
s2.shownumber()

s3=(s1+s2)
s3.shownumber()