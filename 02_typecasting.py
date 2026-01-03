#converting one type to another type

name = "Ashraful"
age= 25
gpa = 3.25
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#convert gpa to int
gpa = int(gpa)
print(gpa)

age= float(age)
print(age)

age = str(age)
age = age+"1"
print(age)
print(type(age))

name = bool(name)
print(name)
