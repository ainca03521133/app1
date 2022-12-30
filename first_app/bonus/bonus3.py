meals = ['pasta', 'pizza', 'salad']

for meal in meals:
    print(meal.capitalize())


for meal in "meals":
    print(meal.capitalize())

""" Coding Exercise 1
Write a program that asks the user to enter the country they are from. If the user enters USA, 
the program prints out Hello. If the user enters the word  India, the program prints out Namaste. 
If the user enters the word Germany, the program prints out Hallo.

Note: Strings are case-sensitive in Python, meaning "germany" and "Germany" are treated as two different 
strings. So, please keep that in mind when writing the program. """

""" 
My way
country= input("Where are you come from?")

country= country.lower()

if country=='usa':
    print("Hello")
if country=='india':
    print('namaste')
if country=='germany':
    print("hallo") """

"class way"
country = input("Where are you come from")

match country:
    case 'usa':
        print("hello")
    case 'india':
        print('Namaste')
    case 'Germany':
        print("Hallo")
""" Coding Exercise 2
Please have a look at the code below:

ingredients = ["john smith", "sen plakay", "dora ngacely"]
Put that line in your IDE and write a for-loop below it. The loop should produce the output below:


Tip:  Use the str.title() method to convert strings to Title Case.

Solution """
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for name in ingredients:
    print(name.title())


