class hello():
    name="harry"

    @classmethod
    def changename(cls,name):
        cls.name=name

s1=hello()
print(s1.name)
s1.changename("rahul")
print(s1.name)