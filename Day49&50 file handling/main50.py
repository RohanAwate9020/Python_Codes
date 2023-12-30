f=open('marks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(',')[0]) 
    m2=int(line.split(',')[1]) 
    m3=int(line.split(',')[2]) 
    print(f'Marks of student {i} in maths:{m1}')
    print(f'Marks of student {i} in maths:{m2}')
    print(f'Marks of student {i} in maths:{m3}')

    print(line)


w=open('marks.txt','w')
lines=['56,79,88\n','23, 43, 66\n','34, 45, 89\n','34,76,44']
w.writelines(lines)
w.close()