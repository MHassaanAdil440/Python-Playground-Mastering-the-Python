num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

operation = input("Enter 1,2,3,4 for +-*/ operations respectively: ")

def add(num1, num2):
    return int(num1) + int(num2)
def subtract(num1, num2):    
    return int(num1) - int(num2)
def multiply(num1, num2):
    return int(num1) * int(num2)
def divide(num1, num2):
    return int(num1) / int(num2)

if operation == '1':
    print("The sum of {0} and {1} is {2}".format(num1, num2, add(num1, num2)))
elif operation == '2':
    print("The difference of {0} and {1} is {2}".format(num1, num2, subtract(num1, num2)))
elif operation == '3':
    print("The product of {0} and {1} is {2}".format(num1, num2, multiply(num1, num2)))
elif operation == '4':
    print("The quotient of {0} and {1} is {2}".format(num1, num2, divide(num1, num2)))
else:
    print("Invalid input")