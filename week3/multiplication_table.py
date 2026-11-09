number = int(input("enter any whole number greater than 1: "))
if number <= 1:
    print("invalid number, enter a number greater than 1")
print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("<=================================================================>")
for multiplier in range(1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

