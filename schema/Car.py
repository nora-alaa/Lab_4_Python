class Car:
    def __init__(self, name, fuelrate, velocity):
        self.name = name
        self.fuelrate = fuelrate
        self.velocity = velocity

    @property
    def fuelrate(self):
        return self.__fuelrate

    @fuelrate.setter
    def fuelrate(self, fuelrate):
        if 0 <= fuelrate <= 100:
            self.__fuelrate = fuelrate
        else:
            print("must be between 0 and 100 so fuelrate will be 0 by default")
            self.__fuelrate = 0

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if 0 <= velocity <= 200:
            self.__velocity = velocity
        else:
            print("must be between 0 and 200 so velocity will be 0 by default")
            self.__velocity = 0

    def run(self, velocity, distance):
        self.__velocity = velocity
        percentDecrease = (distance / 10) * 10
        self.__fuelrate = self.__fuelrate - (1 - (percentDecrease / 100))
        if self.__fuelrate <= 0 or distance == 0:
            self.stop(distance)

    def stop(self, distance):
        self.__velocity = 0
        if distance == 0:
            print("you arrived to your destination")
        else:
            print(f"remain distance to your destination : {distance}")

