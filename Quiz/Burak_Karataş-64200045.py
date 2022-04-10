
a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

discriminant = (b**2) - (4*a*c)

r1 = ((-b) + (discriminant ** 0.5)) / (2*a)
r2 = ((-b) - (discriminant ** 0.5)) / (2*a)

if discriminant < 0:
    print ("Equation has no reel roots.")
elif discriminant == 0:
    print ("Equation has one reel root.")
    print ("Root = ", r1)
elif discriminant > 0:
    print ("Equation has two reel roots.")
    print ("Root 1 = ", r1)
    print ("Root 2 = ", r2)


