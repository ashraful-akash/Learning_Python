#if = do some code if some condition is true
# else do something else

age = int(input("enter your age: "))


if age >= 18:
    print("You can sign up")
elif age < 0 :
    print("You are not born yet. LOL!!")
else:
    print("Not possible to sign up. You must be 18+ to sign up")

response = input("Would You like to order some food ? (Y/N)")

if response == "Y":
    print("Here is your food")
