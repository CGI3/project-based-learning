#Prompts the user to input their age
age = input("What is your current age?")

#Casting age from str to int so we can do calculations on the input
age_input = int(age)

#Setting up variables for input age in days, weeks, and months
age_in_days = age_input * 365
age_in_weeks = age_input * 52
age_in_months = age_input * 12

# Setting up days, weeks, and months in 90 years
days_in_90yrs = 90 * 365
weeks_in_90yrs = 90 * 52
months_in_90yrs = 90 * 12

#Making variables for days, weeks, and months left until you turn 90
days_until_90 = days_in_90yrs - age_in_days
weeks_until_90 = weeks_in_90yrs - age_in_weeks
months_until_90 = months_in_90yrs - age_in_months

#Print out the result
print(f"You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left.")
