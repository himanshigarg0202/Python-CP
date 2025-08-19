#check if the number is divisible by 7 or if the last digit is 5.

n=int(input("enter the number"))
if n % 7 == 0 and n % 10 == 5:
    print("the number is divisible by 7 and last digit is 5")
else:
    print("the number is not divisible by 7 and last digit is 5")