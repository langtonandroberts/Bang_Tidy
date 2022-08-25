
#https://youtu.be/pd-0G0MigUA


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return'{} {}'.format(self.first,self.last)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)
    
    
    
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
