# Exercise 1
# Andrango Ariana and Quiroz Maria

class Calculator():

    def __init__(self):
        self.number1 = float(input("Get into first number: "))
        self.number2 = float(input("Get into second number: "))

    def imprint(self):
        print("The numbers entered are:", self.number1, "and", self.number2)

    def add(self):
        addition = self.number1 + self.number2
        print("Addition is:", addition)

    def subtract(self):  
        subtraction = self.number1 - self.number2
        print("Subtraction is:", subtraction)

    def multiply(self):
        multiplication = self.number1 * self.number2
        print("Multiplication is:", multiplication)

    def split(self):
        if self.number2 == 0:  
            print("Division by zero is not allowed.")
        else:
            division = self.number1 / self.number2
            print("Division is:", division)


micalculadora = Calculator()
micalculadora.imprint()
micalculadora.add()
micalculadora.subtract()
micalculadora.multiply()
micalculadora.split()
