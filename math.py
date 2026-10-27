def find_x_y():
    for x in range(-100, 101):
        for y in range(-100, 101):
            if 3 * x + y == 4 and x + y == 2:
                print(f"Found a solution: x={x}, y={y}")
                return

find_x_y()