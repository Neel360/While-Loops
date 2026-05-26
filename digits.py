num = int(input("Enter the number you want to see how many digits it contains: "))


count = 0

while num != 0:
    num = num//10
    count = count + 1

print(f"Digits: {count}")
