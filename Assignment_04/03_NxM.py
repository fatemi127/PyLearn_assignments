m = int(input("m?\n"))
n = int(input("n?\n"))

print("x", end="\t") 

x = 1
while x <= m:
     print(x ,end="\t")
     x += 1

y = 1
while y <= n:
     print("")
     print(y,end="\t")
     z = 1  
     while z <= m:
          print(y*z ,end="\t") 
          z += 1
     y += 1 
print()