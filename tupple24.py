tu=(1)
print(type(tu))#if we initialize the tuple with the single value then compiler get confusied and take it as an integer variable 

tu1=(1,)
print(type(tu1))#for the above proble just add ,(comma) after the single element.

tup=(1,5,7,3,8,9)
print(type(tup),tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
# print(tup[5])


countries=("India", "Spain","Germany","USA")
print(countries)
cpycunt=list(countries)
cpycunt.append('Russia')
countries=tuple(cpycunt)
print(countries)