a=int(input("Enter value between 5 to 10:"))
if (a<5 or a>10):
    raise ValueError("value should be in between 5 to 10.")