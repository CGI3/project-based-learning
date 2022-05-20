#Prompts the user for their height in meters and weight in kilograms, and converts both to float
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Calculates the users BMI and rounds up
bmi = round(weight / (height ** 2))

#Tells the user whether they are underweight, normal weight, slightly overweight,
#obese, or clinically obese based on their bmi
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
