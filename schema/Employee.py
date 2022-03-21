from schema.Person import Person


class Employee(Person):
    def __init__(self, id, car, email, salary, distancetowork):
        # super.__init__()
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
            self.__salary = 1000

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

    def drive(self):
        pass

    def refuel(self):
        pass

    def send_mail(self, to, subject, msg, receiver_name):
        pass
