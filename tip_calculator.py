#Introduction to program
print("Welcome to the tip calculator!")

#Prompt user for the total bill
bill = input("What was the total bill? $")
usable_bill = float(bill)

#Prompt the user for the tip they want to add
tip = input("How much tip would you like to give? 10, 12, or 15? ")
tip_setup = "1." + tip
tip_amount = float(tip_setup)

#Prompt the user for how many people are splitting the bill
people_paying = input("How many people to split the bill? ")
usable_people_paying = int(people_paying)

#Each person should pay (usable_bill / usable_people_paying) * 1.12 = 33.6
payment_amount = (usable_bill / usable_people_paying) * tip_amount
rounded_payment = round(payment_amount, 2)

#Result rounded to 2 decimal places
print(f"Each person should pay: ${rounded_payment}")
