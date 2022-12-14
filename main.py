#Write a program that tests the compatibility between two people.

#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#we can combine the names, not to check it separately and then add it together.

combined_string = name1 + name2
#Then we can turn everything into lowercase.
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

#So the problem here is that in order to concatenate these two numbers, we had to turn them into strings. 
#So that let's say that the first number is equal to five and the second number was equal to six. 
#Then instead of getting 11, which is not what we want, we actually get 56 because they're both strings and these strings get concatenated together. 
#But the problem occurs on the next step because we wanna compare the love score against an actual numbers (10, 90, 40 and 50), then if it's a string, it's not going to work. 
#So in order to solve this, then we actually have to convert the love score into an integer.

love_score = int(str(true) + str(love))

# Here we're using that logical "or" operator here to check if either this condition or this condition is true.

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

# Below we are using logical "and" operator, where both of these conditions must be true for this statement to fire.

elif love_score >= 45 and love_score <= 55:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")