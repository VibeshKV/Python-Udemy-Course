import math
a = int( input("Enter a: "))
b = int( input("Enter b: "))
c = int( input("Enter c: "))
root1 = (-b+ math.sqrt(b**2-4*a*c))/(2*a)
root2 = (-b- math.sqrt(b**2-4*a*c))/(2*a)
print('roots are', root1, root2)

