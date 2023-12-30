letter = 'Hello, my name is {1}, and I am from {0}'
name="Rohan"
country="India"
print(letter.format(country,name)) 

print('Displaying using an f string\n',f"Hello, my name is {name}, and I am from {country}")
print(f"Hello, my name is {{name}}, and I am from {{country}}")
str=f"Hello, my name is {{name}}, and I am from {{country}}"
print(type(str))