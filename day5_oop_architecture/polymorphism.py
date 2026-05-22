class Payment:
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

payments = [CreditCard(), UPI()]

for p in payments:
    p.pay()

#class method

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))