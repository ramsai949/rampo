class Employee:
    def __init__(self,ename,esal,eid):
        self.ename=ename
        self.esal=esal
        self.eid=eid
    def Display(self):
        print("Employee name: ",self.ename)
        print("Employee esal: ",self.esal)
        print("Employee eno: ",self.eid)

class Test:
    def modify(emp):
        emp.eid+=50
        emp.Display()
e = Employee(45,"sai",25000)
Test.modify(e)



