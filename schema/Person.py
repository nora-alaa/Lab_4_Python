class Person:

    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    @property
    def healthrate(self):
        return self.__healthrate()

    @healthrate.setter
    def healthrate(self,healthrate):
        if 0 <= healthrate <= 100:
            self.__healthrate = healthrate
        else:
            self.__healthrate = 0

    def sleep(self, hours: int):
        if hours == 7:
            self.mood = "happy"
            return True
        elif hours < 7:
            self.mood = "tired"
            return True

        elif hours > 7:
            self.mood = "lazy"
            return True
        else:
            return False

    def eat(self, meals: int):
        if meals == 3:
            self.healthrate = 100
            return True
        elif meals == 2:
            self.healthrate = 75
            return True

        elif meals == 1:
            self.healthrate = 50
            return True
        else:
            return False

    def buy(self, items: int):
        if isinstance(items, int):
            self.money -= 10*items
            return True
        elif items.isdigit():
            self.money -= 10*int(items)
            return True
        else:
            return False
