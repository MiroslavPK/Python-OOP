GROW = 1
SHRINK = -1


def print_rhombus(n):
    direction = GROW

    def print_line(i, direction):
        if i == 0:
            return

        line = (' ' * (n - i)) + ('* ' * i)
        print(line.rstrip())

        if i >= n:
            direction = SHRINK

        print_line(i + direction, direction)

    print_line(1, direction)


print_rhombus(int(input()))
