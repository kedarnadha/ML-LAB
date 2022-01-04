#  Compute the distance travelled by the robot from current position after a sequence of movement and original point.

def finalPosition(move):
    l = len(move)
    countUp, countDown = 0, 0
    countLeft, countRight = 0, 0

    # traverse the instruction string
    # 'move'
    for i in range(l):

        # for each movement increment
        # its respective counter
        if (move[i] == 'U'):
            countUp += 1

        elif (move[i] == 'D'):
            countDown += 1

        elif (move[i] == 'L'):
            countLeft += 1

        elif (move[i] == 'R'):
            countRight += 1

    # required final position of robot
    print("Final Position: (", (countRight - countLeft),
          ", ", (countUp - countDown), ")")


# Driver code
if _name_ == '_main_':
    move = "LD"
    finalPosition(move)

# Output:
# Final Position: ( -1 ,  -1 )
