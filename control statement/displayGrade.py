percentage = float(input("Enter your percentage"))

# Check and print grade based on criteria
if percentage < 0 or percentage > 100:
    print("Please enter a value between 0 and 100")

elif percentage < 25:
    print("Grade: D")

elif percentage <= 45:
    print("Grade: C")

elif percentage <= 65:
    print("Grade: B")

elif percentage <= 85:
    print("Grade: A")

else:
    print("Grade: A+")
