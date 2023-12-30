class Emp:
    def __init__(self,n,id1):
        self.name=n
        self.id=id1

    def showdetail(self):
        print(f'The Emoplyee id of {self.name} is {self.id}')
    
class Prog(Emp):
    def hello(self):
        print('Backend developer')
    
obj=Prog('Rohan',69)
obj.showdetail()
obj.hello()