n=int(input("Enter a number"))
if n <= 0:
    print("Please enter a positive number")
else:
    print(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


 

