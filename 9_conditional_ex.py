#conditional expression = a one line shortcut for if else statement (ternary operator)
#                       print or assign one of the two values based on a condition
#                       X if condition else Y

num = 6
a = 6
b = 7


#print("Positive" if num>0 else "Negative")
result = "Even" if num % 2 == 0 else "ODD"

print (result)

max_num = a if a>b else b
min_num = a if a<b else b

print(max_num)
print(min_num)