from schema.Car import Car
from schema.Person import Person
import re

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

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
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("must be 1000 so salary will be 1000 by default")
            self.__salary = 1000



    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if re.fullmatch(regexEmail, email):
            self.__email = email
        else:
            print("must be well format so email will be none by default")
            self.__email = None

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, car):
        if isinstance(car, Car):
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
        if re.fullmatch(regexEmail, to):
            with open(f"{subject}_to_{to}.txt", 'w') as email:
                message = f"From: {self.email}\n" \
                          f"To: {to}\n" \
                          f"Subject: {subject}\n" \
                          f"" \
                          f"Hi,{receiver_name}\n" \
                          f"{msg}\n" \
                          f"Thanks"
                email.write(message)
