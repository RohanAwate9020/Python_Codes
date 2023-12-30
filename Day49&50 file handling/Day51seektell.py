with open('filr.txt','w') as f:
    f.seek(5)

    print(f.tell())
    f.truncate(6)

