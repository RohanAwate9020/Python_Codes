a=input("Enter a number for multiplication table:")
print(f'Multiplication table of {a} is:')
try:
    for i in range(1,11):
        print(f'{int(a)} X {i} ={int(a)*i}')
except:
    print("Enter integer input only")

