n = int(input("Enter the lenght of snake!\n"))

for i in range (n):
    if n % 2 == 0:
        print("*",end="")
        n -=1
    else:
        print ("#",end= "")
        n -=1