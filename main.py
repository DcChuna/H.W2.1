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
