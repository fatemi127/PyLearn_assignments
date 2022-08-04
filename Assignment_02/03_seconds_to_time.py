seconds = int (input("Enter the seconds: "))
minutes = 0
hours = 0

while seconds > 59:
    seconds -=60
    minutes += 1

while minutes > 59:
    minutes -= 60
    hours += 1

print (f"The time is {hours}:{minutes}:{seconds}")