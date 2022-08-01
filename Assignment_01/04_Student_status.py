from lib2to3.pgen2.token import GREATER


name = input ("Enter Your name:\n")
first = float (input("Enter your first lesson score:\n"))
second = float (input("Enter your second lesson score:\n"))
third = float (input("Enter your third lesson score:\n"))

avg = (first + second + third )/3
if avg >=17:
    status = "Great Score"
elif 17 > avg >= 12:
    status = "Normal Score"
else:
    status = "Fail!"

avg_r = float ("{:.2f}".format(avg))
print (f"Dear {name} Your average is: {avg_r} and you are {status}")
