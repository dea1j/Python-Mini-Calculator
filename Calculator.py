import sys

def add(x, y):
    return x + y
def sub(x, y):
    return (x - y)
def mult(x, y):
    return (x * y)
def divide(x, y):
    return (x / y)

name = input('Please enter your name: ')
print('Welcome', name)
print()
print('Select an Operation to perform')
print('(1)Addition, (2)Subtract, (3)Multiply, (4)Divide or (e)exit')

while True:
    choice = input("Enter choice: ")
    if choice == "e":
            print('Goodbye', name)
            sys.exit()
    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print('Answer =', sub(num1, num2))
        elif choice == '3':
            print('Answer =', mult(num1, num2))
        elif choice == '4':
            print('Answer =', divide(num1, num2))
    else:
        print("Invalid input")
