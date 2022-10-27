class home_Animals:
    def __init__(self):
        self.hignrun = False
        self.fly = False
        self.highjump = False
class Dog(home_Animals):
    def __init__(self):
        super().__init__()
        self.hignrun = True
        self.hignjump = False
        self.fly = False
class Parrot(home_Animals):
    def __init__(self):
        super().__init__()
        self.hignrun = False
        self.hignjump = False
        self.fly = True
class Cat(home_Animals):
    def __init__(self):
        super().__init__()
        self.hignrun = False
        self.hignjump = True
        self.fly = False
d = Dog()
p = Parrot()
c = Cat()
print(('Dog hign run:'), d.hignrun)
print(('Dog hign fly:'), d.fly)
print(('Dog hign jump:'), d.hignjump)
print(('Parrot hign run:'), p.hignrun)
print(('Parrot fly:'), p.fly)
print(('Parrot hign jump:'), p.hignjump)
print(('Cat hign run:'), c.hignrun)
print(('Cat fly:'), c.fly)
print(('Cat hign jump:'), c.hignjump)