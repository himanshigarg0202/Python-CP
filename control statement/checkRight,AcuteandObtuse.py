#Right triangle, Obtuse triangle, Acute triangle

a1 = int(input("Enter first angle: "))
a2 = int(input("Enter second angle: "))
a3 = int(input("Enter third angle: "))

if a1 + a2 + a3 != 180 or a1 <= 0 or a2 <= 0 or a3 <= 0:
    print("Not a valid triangle")
elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Right triangle")
elif a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtuse triangle")
else:
    print("Acute triangle")