n = int(input("How many students?\n"))
scores =[]
for i in range(n):
    score = int (input(f"Enter number {i+1} score:\n"))
    scores.append (score)
average = sum (scores) / len (scores)
max = max (scores)
min = min (scores)

print (f"Max number is: {max}, Min number is: {min} and average is: {average}")