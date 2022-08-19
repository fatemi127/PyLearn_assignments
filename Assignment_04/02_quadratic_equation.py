import math

a = int (input("Enter a:\n"))
b = int (input("Enter b:\n"))
c = int (input("Enter c:\n"))

x = ((-b)+(math.sqrt(abs(b-(4*a*c)))))#/ (2*a)
print (x)