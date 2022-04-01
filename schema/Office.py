from schema import Employee
import json


class Office:
    employeesNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        self.__addToFile()

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        if isinstance(employees, list):
            for e in employees:
                if not isinstance(e, Employee):
                    print("must be list of employees  so employees will be none by default")
                    self.__employees = None
                    break

            self.__employees = employees
            self.in_de_emps_num(len(employees))
        else:
            print("must be list of employees  so employees will be empty list by default")
            self.__employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def __addToFile(self):
        officeData = {self.name: []}
        for emp in self.__employees:
            carDict = vars(emp.car)
            empDict = vars(emp)
            info = {**carDict, **empDict}
            del info["_Employee__car"]
            officeData[self.name].append(info)
        with open("office.json", 'r') as file:
            file_data = json.load(file)
            for index, officeName in enumerate(file_data["office"]):
                nameOfiiceKey = list(officeName.keys())[0]

                if nameOfiiceKey == self.name:
                    del file_data["office"][index]

            file_data["office"].append(officeData)

        with open("office.json", 'w') as filew:
            json.dump(file_data, filew, indent=4)

    @classmethod
    def in_de_emps_num(cls, num):
        cls.employeesNum += num

    def get_all_employees(self):
        return self.__employees

    def get_employee(self, empId):
        for e in self.__employees:
            if e.id == empId:
                return e
            else:
                return False

    def hire(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            self.in_de_emps_num(1)
            self.__addToFile()
        else:
            print("can't hire, must be instance of employee")

    def fire(self, empId):
        for index, emp in enumerate(self.__employees):
            if emp.id == empId:
                del self.__employees[index]
                self.in_de_emps_num(-1)
                self.__addToFile()
                break

    def calculate_lateness(self, empId, moveHour):
        for emp in self.__employees:
            if emp.id == empId:
                if self.check_lateness(9, moveHour, emp.distance, emp.car.velocity):
                    emp.salary -= 10
                else:
                    emp.salary += 10

    @staticmethod
    def check_lateness(targetHour, moveHour, distance, velocity):
        time = distance / velocity
        if moveHour + time < targetHour:
            return False
        else:
            return True

    def deduct(self, empId, deduction):
        for e in self.__employees:
            if e.id == empId:
                e.salary -= deduction
            else:
                print(f"can't find this employee with id : {empId}")

    def reward(self, empId, reward):
        for e in self.__employees:
            if e.id == empId:
                e.salary += reward
            else:
                print(f"can't find this employee with id : {empId}")
