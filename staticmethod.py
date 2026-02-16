class hello:
    def __init__(self):
     print("hello")
    @staticmethod #decorator
    def hello1():
        print("hello static method")


s1=hello()
s1.hello1()
