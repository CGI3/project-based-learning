# Asks the user for the year that they want to check for - whether it's a leap year or not.
year = int(input("Which year do you want to check? "))

# If the year is divisible by 4, move to next if.
if year % 4 == 0:
# If the year is divisible by 4 and 100, move to next if.
  if year % 100 == 0:
# If the year is divisible by 4, 100, and 400, it's a leap year
    if year % 400 == 0:
      print("Leap year.")
# If the year is divisible by 4 and 100, but not 400, it's not a leap year
    else:
      print("Not leap year.")
# If the year is divisible by 4, and not divisible by 100, it's a leap year
  else:
    print("Leap year.") 
# If the year is not divisible by 4, it's not a leap year.
else:
  print("Not leap year.")
