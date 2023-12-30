import os

filename=os.listdir('Excercise 7')
print(filename)
j=0

for f in filename:
    x=list(f.split("."))
    if x[1]=="png":
        os.rename(f'Excercise 7/{f}',f'Excercise 7/{j}.png')
        j+=1
  