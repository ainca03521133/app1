def get_water(temperature):
    if temperature >= 100:
        print("Gas")
    elif temperature<0:
        print("Ice")
    elif temperature>0 and temperature<100:
        print("Water")
