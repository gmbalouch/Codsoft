#TASK 2
#CALCULATOR
#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("\n------Simple Calculator------")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(x)")
    print("4. Division(/)")
    choice = input("Enter choice: ")
    
    print("--------------------------------")
    
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid input. Please enter a valid operation choice."

    
    print(f"Result: {result}")


while True:
   calculator()
   con = input("Do you want to continue? (yes/no): ")
   if con.lower()!='yes':
            break