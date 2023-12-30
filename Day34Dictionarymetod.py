ep1={1:'Rohan',2:'Omkar',3:'Nikhil'}
ep2={4:'Prathmesh',5:'Pratik'}
print('ep1:',ep1)
print('ep2:',ep2)
ep1.update(ep2)#ep2 data get append in ep1 but also remain in ep2
print('ep1 after update:',ep1)
print('ep2:',ep2)
ep1.pop(3)
print('ep1 after pop funtion on key 3:',ep1)#popitem() removes last key value pair for dict

ep3={'Name':'Avi'}
print('ep3:',ep3)
ep3.clear()
print('ep3 after clear:',ep3)#clears the data form the dictionary 
empt={}
print(type(empt))
del empt#to delete whole dictionary
print(empt)

