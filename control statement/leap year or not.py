#check whether a year is a leap year or not. 

Y = int(input("Enter a year: "))

if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
    print("It is a Leap year")
else:
    print("It is Not a leap year")
