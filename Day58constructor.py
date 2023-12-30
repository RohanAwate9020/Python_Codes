class Sample:

    def __init__(self,n,m):
        self.name=n
        self.marks=m
    
    def info(self):
        print(f'{self.name} has {self.marks}  marks.')


class s2:

    def __init__(self):
        print('This is default constructor.')


a=Sample('Rohan',90)
a.info()

b=s2()