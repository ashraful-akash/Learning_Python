# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#              *unpacking operator
#               1. positional. 2. default 3.keyword 4. ARBITRARY

def add(a,b):
    return a+b

print(add(1,2))


def add(*args):
    total = 0
    for arg in args:
        total +=arg
    return total

print(add(1,2,3))


def display_name(*args):
    for arg in args:
        print(arg, end =" ")
display_name("Dr","Spongebob","Harold","Squarepants","III")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end =" ")
    print()
    print (f"{kwargs.get('street')}")
    print (f"{kwargs.get('city')}")
    print (f"{kwargs.get('state')}")
    print (f"{kwargs.get('zip')}")

shipping_label("Dr","Spongebob","Squarepants","III",
               street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")