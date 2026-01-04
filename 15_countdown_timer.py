import time

my_time = int(input("Enter the time in seconds: "))

# for x in range(0,my_time):
#     print(x)
#     time.sleep(1)

# print("Times up!")



# #reversed
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)

# print("Times up!")


# #stopwatch with hours mins and seconds

for x in range(my_time, 0, -1):
    seconds = x % 60
    mins = int (x/60) % 60
    hrs = int(x/3600)
    print(f"{hrs:02}:{mins:02}:{seconds:02}")
    time.sleep(1)
print("Times up!")