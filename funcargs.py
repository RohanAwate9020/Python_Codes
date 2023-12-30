#Required argument
def average(c,d):
    print('average of' ,c,'and',d,'is:',(c+d)/2)

a=2
b=4
average(a,b)



#default arguments
def sum(a=3, b=5):
    print("Sum of two numbers is:",a+b)

sum()

def name(fname, mname='Bhaurao',lname='Awate'):
    print('Hello Mr.',fname ,mname ,lname)

name('Rohan')



#Keyword Argument(We can change the order of argument.)
def name(fname, mname,lname):
    print("Example of Keyword Aegument:")
    print('Hello Mr.',fname ,mname ,lname)

name(lname='Awate',fname='Rohan', mname='B.')



#Variable length argument(When we want to pass multiple arg.):
def avg(* num):
    sum=0
    for i in num:
        sum=i+sum
    print("Avg:",sum/len(num))

avg(2,43,7,5,8,8.9)



#Return Statement 
def avg(* num):
    sum=0
    for i in num:
        sum=i+sum
    return sum/len(num)

c= avg(95,87,45,32,7)
print(c)








