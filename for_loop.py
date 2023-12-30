name = 'Rohan'
for i in name:
    print(i)
    if i=='o':
        print("||| Hello world |||")

colors = ['Red', 'Blue', 'Black', 'White']
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k+1)
for k in range(1,10,1):
    print(k)

for i in range(1,11,1):
    print('table of',i)
    for k in range(1,11,1):
        print (i,'*',k,'=',i*k)
    print('\t')