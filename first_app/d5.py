wating_list = ["sen", "ben", "john"]
wating_list.sort()#SORT 會直接改變LIST裡的排訊

for i, item in enumerate(wating_list):
    row = f"{i+1}.{item.capitalize()}"
    print(row)

""" Coding Exercise 1
Please have a look at the filenames list below:

filenames = ['document', 'report', 'presentation']

Place the list in a .py file and extend the code so it prints out the output below: """
filenames = ['document', 'report', 'presentation']


for index, item in enumerate(filenames):
    row = F"{index}-{item.capitalize()}.txt"
    print(row)

""" Coding Exercise 2
Please place the ips list in a .py file:

ips = ['100.122.133.105', '100.122.133.111']

Your task is to create a program that lets the user enter an index and the program returns the IP address with that index.

Here is how the program would behave when executed: """

ips = ['100.122.133.105', '100.122.133.111']

search= int(input("Enter the index of the IP you want: "))
print(F"You chose {ips[search]}")


usernames = ["john 1990", "alberta1970", "magnola2000"]

surnames=[len(name) for name in usernames]
print(surnames)

user_entries = ['10', '19.1', '20']
user = [float(number) for number in user_entries]
print(user)

user_entries = ['10', '19.1', '20']
user = [float(number) for number in user_entries]
print(sum(user))
