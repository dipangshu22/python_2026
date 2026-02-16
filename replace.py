f=open("hello.txt","r")
data=f.read()

newdata=data.replace("java","python")
print(newdata)

with open("hello.txt","w")as f:
    f.write(newdata)
