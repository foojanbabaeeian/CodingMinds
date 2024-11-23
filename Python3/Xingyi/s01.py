class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def talk(self):
        print(self.name, "is talking")


fluffy = Cat("fluffy", 12, "orange")
print(fluffy.age)
fluffy.talk()

boo = Cat("Boo",  12, "orange")
print(boo.name)
