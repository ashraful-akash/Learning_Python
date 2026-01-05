fruits = ["apple","orange","banana","coconut"]
veg =    ["celery","carrots","potatoes"]
meats =  ["chicken","fish","turkey"]

groceries = [fruits,veg,meats]

# fruits[0]="pineapple"
# print(fruits)

#print(groceries[2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


#creating num pad

num_pad =((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))

print(num_pad)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()