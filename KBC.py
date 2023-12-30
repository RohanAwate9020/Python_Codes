que =["Grand Central Terminal, Park Avenue, New York is the world",'Entomology is the science that studies','Garampani sanctuary is located at']
opt =['largest railway station','highest railway station','longest railway station','None of the above','Behavior of human beings','Insects',"The origin and history of technical and scientific terms",'The formation of rocks',
      'Junagarh, Gujarat','Diphu, Assam','Kohima, Nagaland','Gangtok, Sikkim']
ans=['largest railway station','Insects','Diphu, Assam']

for i in que:
    k=que.index(i)
    print("Oue No",k+1,':',i)
    temp=k*4
    num=1
    for i in range(temp,temp+4):
        print(num,opt[i])
        num=num+1
    ansinput=int(input("Enter the correct option number:"))
    if opt[temp+(ansinput-1)]==ans[k]:
        print("Correct answer")
    else:
        print ("Wrong option")
        print("You won",50000*k,'Rs')
        break
    
    