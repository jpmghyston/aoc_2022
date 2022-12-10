def print_screen(screen):
    for line in screen:
        print("".join(line))


with open("day_10/day10_input.txt") as f:
    instructions = list(reversed([x.strip().split(" ") for x in f.readlines()]))

register = 1
addNextCycle = []

screen = [["." for _ in range(40)] for _ in range(6)]
        
relevantCycles = set([20, 60, 100, 140, 180, 220])
signalStrengths = []
cycle = 0

while len(instructions) > 1:
    pixel_x = cycle % 40
    pixel_y = cycle // 40
    if register - 1 <= pixel_x <= register + 1:
        screen[pixel_y][pixel_x] = "#"
    cycle += 1
    if cycle in relevantCycles:
        signalStrengths.append(cycle * register)
    if len(addNextCycle) > 0:
        register += addNextCycle.pop()
    else:
        match instructions.pop():
            case ["noop"]:
                pass
            case ["addx", val]:
                addNextCycle.append(int(val))


print(sum(signalStrengths))
print_screen(screen)
