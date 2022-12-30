def initializeBoard():
    board = [
        [3, 2, 1],  # initial configuration of the disks
        [],
        []
    ]
    return board
def printBoard(board):
    print("Tower 1: ", board[0])
    print("Tower 2: ", board[1])
    print("Tower 3: ", board[2])

def checkInput(src, dest):
    if src < 1 or src > 3 or dest < 1 or dest > 3:
        print("Please enter a valid tower number.")
        return False
    elif src == dest:
        print("Please enter two different towers.")
        return False
    else:
        return True

def moveDisk(board, src, dest):
    disk = board[src-1].pop()
    board[dest-1].append(disk)

board = initializeBoard()
while len(board[2]) < 3:
    printBoard(board)
    src = int(input("Enter the source tower: "))
    dest = int(input("Enter the destination tower: "))
    if checkInput(src, dest):
        moveDisk(board, src, dest)
print("Congratulations, you have won the game!")


