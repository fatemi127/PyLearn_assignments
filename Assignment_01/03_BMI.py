h = float (input ("Enter your height (Example: 1.82)\n"))
w = float (input ("Enter your weight! (Example: 85.5)\n"))
bmi = (w/h**2)
if bmi >= 35:
    status = "Extremely Obese"
elif 35 > bmi >= 30:
    status = "Obese"
elif 30 > bmi >= 25:
    status = "Over Weight"
elif 25 > bmi >= 18.5:
    status = "Normal"
else:
    status = "Underweight"

print ("Your bmi is ",float("{:.2f}".format(bmi)),"And you are in",status,"status")