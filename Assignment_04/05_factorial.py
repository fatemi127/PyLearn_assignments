n = int(input("Enter the number:\n"))
counter = 1
while n>=counter:
    fact = 1
    for i in range(1, counter+1):
        fact *= i
    if fact == n:
        print("yes")
        break
    counter += 1
else:
    print("No")        

