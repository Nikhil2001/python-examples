class Employee:
    number=0
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
        Employee.number+=1

    def raisepay(self):
        self.pay=self.pay*1.04
        return self.pay



nik=Employee("nikhil",23,10000)
print nik.pay
print nik.raisepay()
print Employee.number
nik1=Employee("mara",33,20000)
print Employee.number
print nik.__dict__
