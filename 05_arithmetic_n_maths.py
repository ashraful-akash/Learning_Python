import math

cakes = 5

#cakes = cakes + 1
#cakes +=1

#cakes = cakes -2
#cakes -= cakes

#cakes = cakes * 3
#cakes *= cakes

#cakes = cakes / 2
#cakes /=2

#cakes = cakes ** 2
#cakes **= 2

#remainder=cakes % 3
cakes %=3

print(cakes)



x = 3.14
y = 4
z = 5
#result = round(x)
#result = abs (y)
#result = pow(2,3)

result = min(x,y,z)
print(result)

m=9.1

print(math.pi)
print(math.e)

res = math.sqrt(m)
print(res)

ceil = math.ceil(m)
print (ceil)

floor = math.floor(m)
print (floor)
 
#c = 2 pie r
radius = float(input("enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is : {round(circumference,2)}")

# area of a circle

area = math.pi * pow (radius,2)
print(f"The area of the circle is : {round(area,2)}")
