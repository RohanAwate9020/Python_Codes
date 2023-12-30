# READING A FILE
f=open('myfile.txt','r')
# print(f)
content=f.read()
print(content)
f.close()

# WRITING A FILE
# USING A WRITE() PREVIOUS FILE CONTENT GOT REMOVE AND THE NEW CONTENT GET REPLACED IN THAT. AND ASLO IT CREATES AN FILE IF FILE DOES'NT EXISTS.
f1=open('myfile.txt','w')
f1.write('Hello eveyone :)')
f1.close()



