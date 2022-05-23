print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Change the names to lowercase so it's easier to find the number of letters
lowercase_name1 = str(name1.lower())
lowercase_name2 = str(name2.lower())

# These variables count the individual letters in "True Love" in Name1
name1_t_count = lowercase_name1.count('t')
name1_r_count = lowercase_name1.count('r')
name1_u_count = lowercase_name1.count('u')
name1_e_count = lowercase_name1.count('e')
name1_l_count = lowercase_name1.count('l')
name1_o_count = lowercase_name1.count('o')
name1_v_count = lowercase_name1.count('v')
name1_second_e_count = lowercase_name1.count('e')

# These variables count the individual letters in "True Love" in Name2
name2_t_count = lowercase_name2.count('t')
name2_r_count = lowercase_name2.count('r')
name2_u_count = lowercase_name2.count('u')
name2_e_count = lowercase_name2.count('e')
name2_l_count = lowercase_name2.count('l')
name2_o_count = lowercase_name2.count('o')
name2_v_count = lowercase_name2.count('v')
name2_second_e_count = lowercase_name2.count('e')

#This variable gets the total number of letters in "True" from both names
total_true_count = name1_t_count + name1_r_count + name1_u_count + name1_e_count + name2_t_count + name2_r_count + name2_u_count + name2_e_count

#This variable gets the total number of letters in "Love" from both names
total_love_count = name1_l_count + name1_o_count + name1_v_count + name1_second_e_count + name2_l_count + name2_o_count + name2_v_count + name2_second_e_count

#This variable makes the totals above into a concatenated string, then turns that concatenated string into an int
love_score = int(str(total_true_count) + str(total_love_count))

#This if conditional is giving a score to the users based on the int from love_score
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")  
else:
  print(f"Your score is {love_score}.")  
