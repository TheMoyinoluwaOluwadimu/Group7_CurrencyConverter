def Sum(a, b):
    return a + b


def Subtraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    return a / b


# User Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function to get the
Total = Sum(num1, num2)
Difference = Subtraction(num1, num2)
Product = Multiplication(num1, num2)
division = Division(num1, num2)

print(f"sum = {Total}")
print(f"Difference=  {Difference}")
print(f"Product= {Product}")
print(f"Division = {division} ")
