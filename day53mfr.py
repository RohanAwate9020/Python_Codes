#MAP
def cube(x):
    return x*x*x

l=[1,5,7,3,8]

ansl=list(map(cube,l))#we give function name and list to map fucntion and it gives us ans wich is performed on each element of passed list.
#we can also use lambda function insted of cube() for ex.
#ansl=list(map(lambda x: x*x*x, l))
print(ansl)


#FILTER
def filter_f(a):
    return a>100

newl=list(filter(filter_f,ansl))
print(newl)
