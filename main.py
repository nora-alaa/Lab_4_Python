from schema.Employee import Employee
from schema.Car import Car
from schema.Office import Office

# id, car, email, salary, distancetowork, name, money, mood, healthrate
# name, fuelrate, velocity
# name, employees
myCar = Car("fiat 128", 50, 50)
myCar2 = Car("nissan 8", 30, 10)
myCar3 = Car("fiat 8", 100, 90)

emp1 = Employee(1, myCar, "n@n.com", 3000, 20, "nora", 5000, "tired", 50)
emp2 = Employee(2, myCar2, "d@d.com", 4000, 60, "doaa", 6000, "happy", 50)
emp3 = Employee(3, myCar, "d@sds.com", 4000, 60, "dossaa", 6000, "happy", 50)
emp4 = Employee(4, myCar3, "dbb@sbds.com", 4000, 60, "bbbaa", 6000, "happy", 50)

emps = [emp1, emp2]
iti = Office("iti", emps)

emps2 = [emp4, emp3]
tel = Office("tel", emps2)

iti.hire(emp3)
iti.fire(3)


print(Office.employeesNum)
