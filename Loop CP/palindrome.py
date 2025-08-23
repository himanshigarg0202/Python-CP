#palindrome or not

A = input("Enter a number")
if A == A[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")
