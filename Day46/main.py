import os 

if (not os.path.exists('Data')):
    os.mkdir('Data')

for i in range(0,30):
    os.mkdir(f"Data/Day {i}")
    os.mkdir(f"Data/Day {i}/main.py")

for i in range(0,30):
    os.rename(f"Data/Day {i}",f"tutorial {i}")

folders=os.listdir('Data')
print(folders)
for f in folders:
    print(f)
    print(os.listdir(f'Data/{f}'))

print(os.getcwdb())

for i in range(0,30):
    os.rmdir(f"Data/Day {i}")
    os.rmdir(f"Data/tutorial {i}/main.py")
    os.rmdir(f"Data/tutorial {i}")

