# where you have to take N as input from the user. 

n = int(input("Enter a positive integer: "))
if n > 0:
    for i in range(n, 0, -1):
        print(i, end=' ')
