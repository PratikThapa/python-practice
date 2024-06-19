 #Creating global constants named as ADDITON, SUBTRACTION, MULITPLICATION, DIVISON
ADDITION = "+"
SUBTRACTION = "-"
MULTIPLICATION = "*"
DIVISION = "/"

#Greet the user
#Name variable to enter user input
Name = input("Enter your name: ")
print ("Hello " + Name + ", Welcome to Simple Calculator")

try:
    number1  = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))
except ValueError:
    print("Error!! Please enter the numeric input.")
    exit()
    
operation = input("Please select an operation to be performed (+, -, *, /): ")

# Perform arithmetic operations
def User_Operation(number1, number2, operation):
    if operation == ADDITION:
        result = number1 + number2
        return result
    elif operation == SUBTRACTION:
        result = number1 - number2
        return result
    elif operation == MULTIPLICATION:
        result = number1 * number2
        return result
    elif operation == DIVISION:
        if number2 != 0:
            result = number1 / number2
            return result
        else:
            print("Cannot be divided by zero.")
            exit()
    else: 
        print("Cannot perform the requested operation. Please select an operation (+, -, *, /)")
        exit()

output = User_Operation(number1, number2, operation)

#Display the result
print("The required result is " + str(output))
    
