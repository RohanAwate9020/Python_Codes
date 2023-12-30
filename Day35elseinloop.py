for i in range(6):
    print(i)
else:
    print('6 is not available in loop')
#else part is executed when the execution of for loop or while loop completed and program only gets exit when the else block is executed

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print('6 is not available in loop')
'''the execution of loop of break in between so thats why the exeution of loop is not completed
hence the last value is not processed so the else block is not get execute becuase
loop is break not completed'''