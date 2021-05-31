#Multiple inheritance occurs when the child class
# inherits from more than one parent class.
class employee:
    company = " Amazon"
    ecode = 120
    def upgradeecode(self):
        self.ecode = self.ecode+2
class freelancer:
    company = "Fiverr"
    level = 10
    def upgradelevel(self):
        self.level = self.level+2

class programmer(employee,freelancer):
    name = "ahadraza"

p = programmer()
p.upgradelevel()
print(p.level)

p1 = freelancer()
p1.upgradelevel()
print(p1.upgradelevel)

p2 = employee()
p2.upgradeecode()
print(p2.ecode)