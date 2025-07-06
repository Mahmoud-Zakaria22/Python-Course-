def Calculator(a,b,operation):
    if operation=="Sum":
        return a+b
    elif operation=="subtract":
        return a-b
    elif operation=="multiply":
        return a*b
    elif operation=="divide":
        return a/b
    else:
        "Enter the right operation"

print(Calculator(5,24,"Sum"))

