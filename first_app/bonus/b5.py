""" date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thought = input ("Let your thoughts flow:\n")

with open(r"first_app\files\{}.txt".format(date), "w") as file:
    file.write(mood + 2* "\n")
    file.write(thought)
 """

coin = input("Throw the coin and enter head or tail here: ?")
match coin:
    case "head":
        possibilty = int(1)
    case "tail":
        possibilty = int(0)
Throw_coin = []
Throw_coin = Throw_coin.append(coin)

with coin as Throw_coin:
    rlpossibilty=sum(Throw_coin)/len(Throw_coin+1)
    print("heads:"+ str(rlpossibilty))



