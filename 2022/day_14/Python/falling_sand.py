import numpy as np

def read_file(path="../input.txt"):
    with open(path) as file:
        return file.readlines()

def interpret_input(lines):
    """
    Turn the list of lines into a usable input.
    A big numpy array with 0 for air and 1 for rock.
    """
    xmax, ymax = (0,0)
    instructions = []

    for line in lines:
       instruction = interpret_line(line)
       xmax = max(np.max(instruction[:,0]), xmax)
       ymax = max(np.max(instruction[:,1]), ymax)

       instructions.append(instruction)

    cave = np.zeros((xmax+2, ymax+2), dtype=int)

    for instruction in instructions:
        for pt1, pt2 in zip(instruction, instruction[1:,:]):
            xlow, xhigh = sorted((pt1[0], pt2[0]))
            ylow, yhigh = sorted((pt1[1], pt2[1]))
            cave[xlow:xhigh+1, ylow:yhigh+1] = 1

    return cave
    

def interpret_line(line:str):
    """
    Interpret a single line into a 2d array of coordinates
    """
    coordinates = line.split(" -> ")
    return np.array([np.array(coordinate.split(","), dtype=int) for coordinate in coordinates])

def drop_sand(cave):
    """
    Spawn a sand at 500,0 and make it fall
    Falling sand is 2
    """
    cave[500,0] = 2

    cave = sand_falls(cave)
    

def sand_falls(cave):
    """
    All sand (2) falls. Direction priority is down (+y), down left (-x+y) then down right (+x+y).
    """



lines = read_file("../input_sample.txt")
cave = interpret_input(lines)
print(cave.shape)
print(cave[490:,:].T)