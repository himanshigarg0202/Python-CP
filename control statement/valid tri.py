#valid tri or not
a = int(input("Enter angle A: "))
b = int(input("Enter angle B: "))
c = int(input("Enter angle C: "))

if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("triangle is valid")
else:
    print("triangle is NOT valid")
