try:
    a = float(input("Enter the number: "))
except ValueError:
    print("Invalid input: please enter a number")
else:
    if a >= 80:
        print("A grade")
    elif a >= 30:
        print("B grade")
    else:
        print("You are failed")
