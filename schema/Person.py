personMode = ("happy", "tired", "lazy")


def containsMood(val):
    for pMood in personMode:
        if val == pMood:
            return True
    return False


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
    def healthrate(self, healthrate):
        if 0 <= healthrate <= 100:
            self.__healthrate = healthrate
        else:
            print("must be between 0 and 100 so healthrate will be 0 by default")

            self.__healthrate = 0

    @property
    def mood(self):
        return self.mood()

    @mood.setter
    def mood(self, mood):
        if containsMood(mood):
            self.__mood = mood
        else:
            print("must be in (happy, tired, lazy) so mood will be null by default")

            self.__mood = None

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
            self.money -= 10 * items
            return True
        elif items.isdigit():
            self.money -= 10 * int(items)
            return True
        else:
            return False
