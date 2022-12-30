""" passwd = input("Enter new password: ")
result = {}

if len(passwd) >=8:
    result["length"] = True 
else:
    result["length"] = False

digit = False
for i in passwd:
    if i.isdigit():
        digit = True

result["digits"] = True 

uppercase = False

for i in passwd:
    if i.isupper():
        uppercase = True
result["upper-case"] = uppercase

print(result)

if all(result) == True:
    print("Strong Password!")
else:
    print("Weak Password!") """


