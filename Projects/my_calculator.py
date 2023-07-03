num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

operation = input("Enter 1,2,3,4 for +-*/ operations respectively: ")

if operation == '1':
    sum = float(num1) + float(num2)
    print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
elif operation == '2':
    difference = float(num1) - float(num2)
    print("The difference of {0} and {1} is {2}".format(num1, num2, difference))
elif operation == '3':
    product = float(num1) * float(num2)
    print("The product of {0} and {1} is {2}".format(num1, num2, product))
elif operation == '4':
    quotient = float(num1) / float(num2)
    print("The quotient of {0} and {1} is {2}".format(num1, num2, quotient))
else:
    print("Invalid input")