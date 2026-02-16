class toyato:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class car(toyato):  #single inheritance ,including all the methods of the parent.
    def __init__(self,name):
        self.name=name

s1=car("fortuner")

print(s1.name)
s1.start()
s1.stop()