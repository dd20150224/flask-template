from angela.library import turn_right, turn_around, move_by

set_max_nb_steps(3000)

SOUTH = "south"
EAST = "east"
NORTH = "north"
WEST = "west"


def outputPos(pos):
    print("   x = " + str(pos[0]))
    print("   y = " + str(pos[1]))
    print("   dir = " + pos[2])


def build_wall_right():
    turn_right()
    build_wall()
    turn_left()


def window_on_right():
    move()
    result = not right_is_clear()
    turn_around()
    move()
    turn_around()
    return result


def update_pos(pos):
    (x, y, direction) = pos
    if direction == EAST:
        x += 1
    elif direction == SOUTH:
        y += 1
    elif direction == WEST:
        x -= 1
    else:
        y -= 1
    result = (x, y, pos[2])
    #    print("update_pos:")
    #    outputPos(result)
    return result


def update_turn_left(pos):
    (x, y, direction) = pos
    if direction == EAST:
        direction = NORTH
    elif direction == SOUTH:
        direction = EAST
    elif direction == WEST:
        direction = SOUTH
    elif direction == NORTH:
        direction = WEST
    result = (x, y, direction)
    #    print("update_turn_left:")
    #    outputPos(result)
    return result


def update_turn_right(pos):
    (x, y, direction) = pos
    if direction == EAST:
        direction = SOUTH
    elif direction == SOUTH:
        direction = WEST
    elif direction == WEST:
        direction = NORTH
    elif direction == NORTH:
        direction = EAST
    result = (x, y, direction)
    #    print("update_turn_right:")
    #    outputPos(result)
    return result


def update_turn_around(pos):
    (x, y, direction) = pos
    if direction == EAST:
        direction = WEST
    elif direction == SOUTH:
        direction = NORTH
    elif direction == WEST:
        direction = EAST
    elif direction == NORTH:
        direction = SOUTH
    result = (x, y, direction)
    #    print("update_turn_around:")
    #    outputPos(result)
    return result


def check_window_on_right(pos):
    move()
    pos = update_pos(pos)

    isRightClear = not right_is_clear()

    turn_around()
    pos = update_turn_around(pos)

    move()
    pos = update_pos(pos)

    turn_around()
    pos = update_turn_around(pos)

    result = isRightClear, pos
    #    print("check_window_on_right:")
    #    print("    isRightClear = " + ("Yes" if isRightClear else "No"))
    #    outputPos(pos)
    return result


def check_side(pos):
    x = 0
    target = False
    while True:
        print(target)
        while not wall_in_front():
            move()
            pos = update_pos(pos)
            if right_is_clear():
                if pos[0] == 0 and pos[1] == 0:
                    target = True
                    break
                window_on_right, pos = check_window_on_right(pos)
                if window_on_right:
                    turn_right()
                    build_wall()
                    turn_left()
                else:
                    turn_right()
                    pos = update_turn_right(pos)
                    move()
                    pos = update_pos(pos)
        if target:
            break
        if wall_on_right():
            turn_left()
            pos = update_turn_left(pos)


move_by(3)

turn_right()
pos = (0, 0, "south")

move()
pos = update_pos(pos)
check_side(pos)

# turn_left()
# check_side()
# turn_left()
# check_side()
# turn_left()
# check_side()

# turn_left()
# move()
# move()


                                                            wai hung chan
wai hung chan

Administrator
orion
