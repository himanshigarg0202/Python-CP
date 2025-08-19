n=int(input( "Enter the number"))

if n == 0:
    print("The number has 1 digit")
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
        print("The number of digit:",count)
        