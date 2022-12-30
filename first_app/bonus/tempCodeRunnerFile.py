year_of_birth= input("Enter your birthyear")
 
def calculate(year_of_birth, current_year= int(2022)):
    age = current_year- int(year_of_birth)
    return age
age = calculate(year_of_birth)

if age >120:
    print("old damn")
else:
    print(age)