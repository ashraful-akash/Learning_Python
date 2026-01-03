# or and not

temp = 30
is_raining = False

#or
if temp > 35 or temp <0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The event is on!")

#and
is_sunny = True

if temp >=28 and is_sunny:
    print("It's hot outside 🥵")

#not
is_sunny = False

if temp >=28 and not is_sunny:
    print("It's not sunny outside 😔")