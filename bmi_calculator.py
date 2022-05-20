#Prompts the user for their weight in kg and height in m, and casts both so operands can be used on them
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

#Calculates BMI (BMI = weight / (height ** 2))
#Casts as an int for whole number
bmi = int(weight / (height ** 2))

#Printing the users bmi
print(bmi)
