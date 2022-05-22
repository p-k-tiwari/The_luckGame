import math
a = float(input("Enter a"))
b = float(input("Enter b"))
c = float(input("Enter c"))
d = (b**2) - (4*a*c)

if d<0 :
     print("Roots are imagenary" )
elif d==0 :
     sq= math.sqrt(d)
     root = (-b - sq)/2*a
     root2 = (-b + sq)/2*a
     print("Roots are real and equal", root, root2)
else:
     sq= math.sqrt(d)
     root = (-b - sq)/2*a
     root2 = (-b + sq)/2*a
     print("Roots are real and unequal", root, root2)
