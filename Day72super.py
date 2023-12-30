class Parent:
    def parentfun(self):
        print('This is an parent class.')

class Child(Parent):
    def chlidfun(self):
        super().parentfun()
        print('This is child class.')
        


obj=Child()
obj.chlidfun()
