""" try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter retangle length: "))
    if width == length:
        exit("The looks like a squre. ")
    area = width*length
    print(area)
except ValueError:
    print("please enter a number") """


""" 
try:
    n1 = float(input("Enter total value:"))
    n2 = float(input("Enter value: "))

    print("That's "+str(float(n2/n1)*100)+"%")
except ValueError:
    print("You need enter a number, Run the program again. ")
except ZeroDivisionError:
    print("Your total value cannot be zero.") """
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")   
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} not in list")

