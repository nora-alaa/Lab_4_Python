from schema.Person import Person


class Employee(Person):
    def __init__(self, id, car, email, salary, distancetowork, name, money, mood, healthrate):
        super().__init__(name, money, mood, healthrate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distancetowork = distancetowork

    @property
    def salary(self):
        return self.__salary()

    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("must be 1000 so salary will be 1000 by default")
            self.__salary = 1000

    @property
    def car(self):
        return self.__car()

    @car.setter
    def car(self, car):
        if isinstance(car, list):
            self.__car = car
        else:
            print("must be car object so car will be none by default")
            self.__car = None

    def work(self, hours: int):
        if hours == 8:
            self.mood = "happy"
            return True
        elif hours < 8:
            self.mood = "tired"
            return True

        elif hours > 8:
            self.mood = "lazy"
            return True
        else:
            return False

    def drive(self, distance):
        self.car.fuelrate(distance, self.car.velocity)

    def refuel(self, gasAmount):
        self.car.fuelrate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        pass
