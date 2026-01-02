#input() = function that promts the user to enter data, 
# returns the enter data as string

name = input("What is your name?: ")
age = int(input("What is your age?:"))
print(f"Hello {name}") #f is used for variables in output
print(f"You are {age} years old")

#Excercise 1 Rectangle Area Calc
length=int(input("Enter the length:"))
width=int(input("Enter the width:"))

area = length * width

print(f"The area of the rectangle is {area}")
