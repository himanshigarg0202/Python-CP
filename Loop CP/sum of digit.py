#calculate sum of digit of number

N = int(input("Enter an number"))
digitsum = sum(int(digit) for digit in str(abs(N)))
print("Sum of digits:", digitsum)