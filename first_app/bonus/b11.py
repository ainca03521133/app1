""" def get_average():
    with open(r"bonus\files\data.txt", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values= [float(i) for i in values]

    average_local = sum(values)/len(values)
    return average_local

average = get_average()
print(average) """

""" def get_max():
    grades = [9.6, 9.2, 9.7]
    new_grade=sorted(grades)
    max_new_grades = new_grade[int(len(new_grade))-1]
    minumum = new_grade[0]
    return print(f"Max is {max_new_grades}, Min is {minumum}")

get_max() """

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    print(maximum)
    return maximum
    
celsius = get_maximum()
 
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)