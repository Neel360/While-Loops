count = 0
num = int(input("Enter a number: "))

while num >= 10:
    num= num/3
    count = count + 1

print(f"Total times divisible by 3 is {count}")
