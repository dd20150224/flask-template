from angela.library import turn_right


def move_and_left(steps=1):
    for i in range(0, steps):
        move()
    turn_left()


def move_and_right(steps=1):
    for i in range(0, steps):
        move()
    turn_right()


def doActionStep(step):
    (actionName, moveCount) = step
    if actionName == "move_and_left":
        move_and_left(moveCount)
    elif actionName == "move_and_right":
        move_and_right(moveCount)


JUMP_ACTION = [("move_and_right", 1), ("move_and_right", 1), ("move_and_left", 1)]


def move_over_hurtle():
    count = 0
    while True:
        turn_right()
        if wall_in_front():
            turn_left()
            move()
            count += 1
        else:
            break
    return count


def jump():
    turn_left()
    steps = move_over_hurtle()
    move()
    turn_right()
    for i in range(0, steps):
        move()
    turn_left()


while True:
    while front_is_clear() and not at_goal():
        move()
    if at_goal():
        break
    jump()
