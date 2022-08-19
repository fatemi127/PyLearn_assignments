a = input("Enter the sentence!\n")
counter = 1
for char in a:
    if char == " ":
        counter +=1
print (f"There are {counter} words.")