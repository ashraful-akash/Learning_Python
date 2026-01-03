#oython_calculator

operator = input("Enter an operator (+ - * /):")

num1 = int(input("Enter your first number: "))
num2= int(input("Enter your second number: "))

if operator == "+":
    sum = num1 + num2
    print(f"Here is your summed number: {sum}")
elif operator =="-":
    abs = num1-num2
    print(f"Your substracted value is: {abs}")
