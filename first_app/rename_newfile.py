filenames =["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)#replace只會跑出結果，需要重新assign一個變數來儲存
    print(filename)
""" Coding Exercise 1
Create a currency converter. The user should be able to enter an amount and get 
the converted currency. You can a currency converter that you wish. For example, 
if the user enters 100, the program should return 95.0: """


money = float(input("How many dollars, Do you have?"))
print("The amount in euros is"+"\n"+ str(money*30))

""" The list indicates that John won 1st place, while Sen got 2nd and Marry the 3rd. 
Users want to know who got what place, so create a program that contains the list above. 
The program lets the user enter a rank number and returns the person who has that rank. 
Here is how the program would behave: """

ranking = ['John', 'Sen', 'Marry']
rank = int(input("Enter rank number: ")) - 1
name = ranking[rank]
print(name)

""" Coding Exercise 3
We have the same list:

ranking = ['John', 'Sen', 'Marry']

This time you need to create a program that lets the user enter the person's name, 
and the program returns the rank that person got. """

ranking = ['John', 'Sen', 'Marry']
name = input("Enter a name :")
rank = int(ranking.index(name))+1
print(rank)