with open("okay.txt","r") as f:
    f.seek(5)

    data=f.read()
    print(data)

