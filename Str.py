apple= "he said,\"i want to eat apple\""
print(apple)

'''Hiii 
this is an example of 
multiline comment.'''

multi='''This is string 
contains data which is 
stored in multiline'''
for i in  multi:
    print(i)


name=('Rohan Awate')

print(name)
print(name[0:5])
print(name[:5])
print(name[6:11])
print(name[0:-6])


nm='Harry!!!!!!!!!!'
# print(nm[-4:-2])
print(nm.strip('!'))
print(nm.upper())
print(nm.lower())
print(nm.replace('Harry',"Rohan"))
blogHeading= 'Introduction to the Python'
print(blogHeading.capitalize())


print(blogHeading)
print(blogHeading.title())
print(blogHeading.center(50))


print(len(blogHeading))
print(len(blogHeading.center(50)))

print(blogHeading.count('t'))
print(blogHeading.endswith('Python'))


# reverse string 
print(blogHeading[::-1])

del blogHeading
print(blogHeading)





