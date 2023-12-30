dict={'Id':1,'Name':'Rohan'}
print(dict)
print(dict['Id'])#gives error if the key does not exist
print(dict.get('Id'))#gives None if the key does not exist

print(dict.keys())#gives all the keys in the dictorinary
for key in dict.keys():
    print(dict[key])

print(dict.values())#gives all  the values in the dictorinary
print(dict.items())#gives all  thekey values pairs in the dictorinary
