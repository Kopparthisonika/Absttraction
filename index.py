from abc import ABC, abstractmethod

# 1. Bank Payment System
class Bank(ABC):
    @abstractmethod
    def pay(self): pass

class UPI(Bank):
    def pay(self): print("Payment using UPI")

class CreditCard(Bank):
    def pay(self): print("Payment using Credit Card")

class NetBanking(Bank):
    def pay(self): print("Payment using Net Banking")

for b in [UPI(), CreditCard(), NetBanking()]:
    b.pay()


# 2. Vehicle System
class Vehicle(ABC):
    @abstractmethod
    def start(self): pass

    def stop(self):
        print("Vehicle Stopped")

class Car(Vehicle):
    def start(self): print("Car Started")

class Bike(Vehicle):
    def start(self): print("Bike Started")

class Bus(Vehicle):
    def start(self): print("Bus Started")

for v in [Car(), Bike(), Bus()]:
    v.start()
    v.stop()


# 3. Employee Salary
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self): pass

    def display(self):
        print("Employee:", self.name)

class FullTimeEmployee(Employee):
    def calculate_salary(self): print("Salary: 50000")

class PartTimeEmployee(Employee):
    def calculate_salary(self): print("Salary: 20000")

class Intern(Employee):
    def calculate_salary(self): print("Salary: 10000")

for e in [FullTimeEmployee("Ravi"),
          PartTimeEmployee("Ram"), Intern("Raj")]:
    e.display()
    e.calculate_salary()


# 4. Shape Area
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    def display(self):
        print("Calculating Area")

class Circle(Shape):
    def area(self): print(3.14 * 5 * 5)

class Rectangle(Shape):
    def area(self): print(10 * 5)

class Triangle(Shape):
    def area(self): print(0.5 * 10 * 5)

for s in [Circle(), Rectangle(), Triangle()]:
    s.display()
    s.area()


# 5. Online Food Ordering
class FoodOrder(ABC):
    @abstractmethod
    def place_order(self): pass

    def order_status(self):
        print("Order is being processed")

class PizzaOrder(FoodOrder):
    def place_order(self): print("Pizza Ordered")

class BurgerOrder(FoodOrder):
    def place_order(self): print("Burger Ordered")

class BiryaniOrder(FoodOrder):
    def place_order(self): print("Biryani Ordered")

for f in [PizzaOrder(), BurgerOrder(), BiryaniOrder()]:
    f.place_order()
    f.order_status()