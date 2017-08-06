class Employee(object):
     number=0
     def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
        Employee.number+=1
class Developer(Employee):
     def __init__(self,name,age,pay,lan):
       super(Developer, self).__init__(name,age,pay)
       self.language=lan
    
nik=Developer("nikhil mara",23,13,"python")
print nik.language

#output: python
