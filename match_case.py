x = int(input("Enter a Number:"))


match x:
    case 0:
        print(x)
    case 1:
        print('1')

    case _ if x<10:
        print("Number is less than 10.")
    case _:
        print('Default Case')