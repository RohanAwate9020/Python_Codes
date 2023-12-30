info = ['C','C++','Python','Html','CSS','JS']
print(len(info))

print(info)

print('0:',info[0])
print('1:',info[1])
print('2:',info[2])
print('3:',info[3])
print('4:',info[4])
print('5:',info[5])

print('Printing with negative indexing:',info[-3])

'''To findout the which index element will be print through negetive indexing
for the findout len by using len(info) and the len(info)-negativeindex
and the result is your index which is positive.
'''
print('Printing by converting negative index into positive:',info[len(info)-3])

if 'C' in info:
    print('Yes')
else:
    print('NO')

'''printing every elemnt in list
print(info)
print(info[:])'''

#printing 1 to 3 elemnt in list
print(info[1:4])

#printing elemnt with the jump index in list means it will skip 2 elemrnt and print 3rd 
print(info[0:6:2])

#list comprehension
lst=[i for i in range (10)]
print(lst)

lst=[i*i for i in range (10)]
print(lst)

lst=[i*i for i in range (10) if i%2==0]
print(lst)