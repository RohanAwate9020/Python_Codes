try:
    a=[1,2,4,6]
    i= int(input("Enter the index"))
    print(a[i])

except:
    print("List index out of bound.")

finally:
    print('I also got executed')
#finally block always get executed no matter error is occoured or not.