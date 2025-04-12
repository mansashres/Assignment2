'''Creating a program called calculator with funcy=tion to perform'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divisible(a,b):
    if b ==0:
        return "Error!Division by zero."
    return a/b
def truncated_divide(a,b):
    if b==0:
        return"Error! Division by zero."
    return a//b
def modulus(a,b):
    if b==0:
        return"Error!Division is zero."
    return a%b
def exponentiate(a, b):
    return a ** b

num1=15.8
num2=3.2

print("Addition:",add(num1,num2))
print("Subtraction:",subtract(num1,num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divisible(num1, num2))
print("Truncated Division:", truncated_divide(num1, num2))
print("Modulus:", modulus(num1, num2))
print("Exponentiation:", exponentiate(num1, num2))

