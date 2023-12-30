class Employee:
    company='TCS'
    def show(self):
        print(f'name of the employee is {self.name} and his company is {self.company}')

    @classmethod
    def changecompany(cls,newcmp):
        cls.company=newcmp
    

e1=Employee()
e1.name="Rohan"
e1.show()
e1.changecompany('Google')
e1.show()
print(e1.company)
print(Employee.company)