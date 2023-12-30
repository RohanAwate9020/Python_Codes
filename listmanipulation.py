l=[34,6,35,7,3,8,91,43,3,65]
print(l)

l.reverse()#Printing list in reverse order
print(l)

l.sort()#ascending order
print(l)

l.sort(reverse=True)#decending sorting
print(l)

print(l.index(35))#printing index of given element 

print(l.count(3))#return count of element


m=l
m[0]=0
print(m)
print(l)#if we copy list into another list and changes are made in new list then changes also refect in older list also to avoid that we copy() ex. given below

p=l.copy()
p[1]=0
print(p)
print(l)

print('\n\n')

l1=[53,5,7,33,65,43]
print(l1)


l1.insert(1,777)#inserting 777 in list l1 at 1st index.
print(l1)

l.extend(l1)
print(l)#this method adds an entire list to the existing list.

l2=l+l1
print(l2)#list concatinate
