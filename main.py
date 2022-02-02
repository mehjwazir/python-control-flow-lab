# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

alpha = input('Please enter a letter from the alphabet (a-z or A-Z)').lower()
vowel = ['a','e','i','o','u','A','E','I','O','U']
if alpha in vowel:
	print(f'The letter {alpha} is a vowel.')
else: 
	print(f'The letter {alpha} is a vowel.')

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ""
while phrase != "quit":
  phrase = input("Please enter a word or phrase: ").lower()
  length = len(phrase)
  if phrase == "quit": break
  print(f" - What you entered is {length} characters long")
	


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

human_years = input("Input a dog's age: ")
human_years = int(human_years)
if human_years < 3:
  print(f"The dog's age in dog years is {human_years * 10}")
else:
  print(f"The dog's age in dog years is {(human_years-2)*7+20}")





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the three lengths of each side of a triangle:")
a = input("a:")
b = input("b:")
c = input("c:")
if a == b == c:
  print(f"A triangle with sides of {a}, {b} & {c} is a equilateral triangle" )
elif a != b != c:
  print(f"A triangle with sides of {a}, {b} & {c} is a scalene triangle" )
else:
  print(f"A triangle with sides of {a}, {b} & {c} is a isosceles triangle" )




# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):


num1 = 0
num2 = 1
for n in range(0, 50):

  if n < 2:
    print(f"term: {n} / number: {n}")
  else:
    current = num1 + num2 
    print(f"term: {n} / number: {current}")
    num1 = num2
    num2 = current
    n += 1


# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

Mmm = input("Enter the month of the year (Jan - Dec):")
dd = int(input("Enter the day of the month:"))

if Mmm in ('Jan', 'Feb', 'Mar'):
	season = 'winter'
elif Mmm in ('Apr', 'May', 'Jun'):
	season = 'spring'
elif Mmm in ('Jul', 'Aug', 'Sep'):
	season = 'summer'
elif Mmm in ('Oct', 'Nov', 'Dec'):
	season = 'fall'

if (Mmm == 'Mar') and (dd > 19):
	season = 'spring'
elif (Mmm == 'Jun') and (dd > 20):
	season = 'summer'
elif (Mmm == 'Sep') and (dd > 21):
	season = 'fall'
elif (Mmm == 'Dec') and (dd > 20):
	season = 'winter'

print(f"{Mmm} {dd} is in {season}")