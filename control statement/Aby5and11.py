#r A is divisible by both 5 and 11 or not

n=int(input("Enter a Number"))

if n % 5 == 0 and n % 11 == 0:
    print("Yes, n is divisible by both 5 and 11.")
else:
    print("No, n is not divisible by both 5 and 11.")