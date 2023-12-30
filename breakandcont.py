
for i in range(1,15,1):
    if (i==11):
        print('loop got terminates over here.')
        break
        
    print(5*i)

for i in range(1,15,1):
    if (i==11):
        print('loop got skip for 11')
        continue
        
    print(5*i)
