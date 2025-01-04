def turn_left():
    print("turn left")


def move():
    print("move")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_and_left(steps=1):
    for i in range(0, steps):
        move()
    turn_left()


def move_and_right(steps=1):
    for i in range(0, steps):
        move()
    turn_right()


def doAction(action):
    (actionName, stepCount) = action
    if actionName == "move_and_left":
        move_and_left(stepCount)
    elif actionName == "move_and_right":
        move_and_right(stepCount)
