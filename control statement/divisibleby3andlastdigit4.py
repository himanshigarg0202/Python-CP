#check if the number is divisible by 3 and the last digit is 4

n = int(input("Enter a number: "))
if n % 3 == 0 and n % 10 == 4:
    print("The number is divisible by 3 and ends with 4")
else:
    print("The number does not satisfy both conditions")