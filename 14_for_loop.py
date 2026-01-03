# foor loops = execute a block of code a fixed number of times
#               you can iterate over a range, string, sequence, etc

for x in range (1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)

for x in range (1,11,3):
    print(x)


credit_card= "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)

for x in range(1,21):
    if x==13:
        break
    else:
        print(x)

