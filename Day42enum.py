l=[1,2,3,4,'R','O','H','A','N','Rohan']
for index,i in enumerate(l):
    print(index,i,'\n\n')
#enumerate function returns a tuple containing the index and value of each elemnt in the sequence.
for index,i in enumerate(l,start=1):#by default the enum starting index is 0 with start parameter we can change it.
    print(index,i)
