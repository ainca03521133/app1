""" content= ["skgskgsdokgpsod",
          "kgsgkopdgkpogd", 
        "dgisgjiosdgsdg"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(content, filenames):
    file = open(r"first_app\files\{}".format(filenames), 'w')
    file.write(content)

Coding Exercise 1
Please download the essay.txt file from the resources of this article. Then, 
create a program that reads that file and prints out its text. 
The first letter of each word in the output should be uppercase. """

file = open(r"first_app\files\essay.txt",'r')
file =file.readline()#read適合看小文件 readline看大文件，皆不會儲存list
print(file.title())#readlines()會把所有數值保存在list獨大文建會站內存 read

""" Coding Exercise 2
Write a program that reads the essay.txt file and returns the number of characters contained in the file.

Solution """

file = open(r"first_app\files\essay.txt",'r')
file =file.readline()#read適合看小文件 readline看大文件，皆不會儲存list
print(len(file))#readlines()會把所有數值保存在list獨大文建會站內存 read

""" file = open("essay.txt", 'r')
content = file.read()

nr_chars = len(content)
print(nr_chars) """

""" Coding Exercise 3
Please download the members.txt file from the resources of this article.

Then, create a program that, whenever executed, asks the user to enter a new member in the command line:


Then, the member is added to members.txt. In this case, the text file content would be:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right """

add_new_member = input("Add a new member:")
file = open(r"first_app\files\members.txt",'r')
member = file.readlines()
file.close()

member.append(add_new_member+ "\n")
file = open(r"first_app\files\members.txt",'w')
member = file.writelines(member)
file.close()

""" 標準解法
member = input("Add a new member: ")

file = open(r"first_app\files\members.txt",'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open(r"first_app\files\members.txt",'w')
existing_members = file.writelines(existing_members)
file.close()
print(file) """

""" Coding Exercise 4
Create a program that generates multiple text files by iterating over the filenames list.
 The text Hello should be written inside each generated text file. """