""" feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 +inches*0.0254
    return meters

result = print(convert(feet_inches))

if result <1 :
    print("Kid is too small")
else:
    print("Kid can use the slide") """

user_password = input("Enter your password: ")

def strength_passwd(passwd):
    result = {}

    if len(passwd) >=8:
        result["length"] = True 
    else:
        result["length"] = False

        digit = False
    for i in passwd:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in passwd:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase
    
    if all(result.values()) :
        return print("Strong password")
    else:
        return print("weak password")

print(strength_passwd(user_password))
    


    
    


