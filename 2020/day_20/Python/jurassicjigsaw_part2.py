from jurassicjigsaw import *
import numpy as np
import os
import matplotlib.pyplot as plt

imagepath = "./2020/day_20/image.txt"
monsterpath = "./2020/day_20/monster.txt"

def get_image():
    """
    Gets image from previously generated file, or generates it if it doesn't exist
    """
    # If image exists, get it and interpret as numpy array
    if os.path.exists(imagepath):
        return load_image(imagepath)
    # otherwise solve the jigsaw
    else:
        # same process as corner_product
        strings = load_string()
        tiles = interpret_tiles(strings)
        solution = solve(tiles)
        # tile together images from tiles
        image = np.vstack([np.hstack([tile.image() for tile in row]) for row in solution])
        # Save to file
        save_image(image)
        return image

def load_image(path):
    """
    Loads an image from the path and retrns a boolean array
    """
    with open(path, "r") as file:
        body = file.readlines()
    content = [list(row.strip()) for row in body]
    content = np.array(content)
    return content == "#"

def save_image(img):
    """
    Saves an image to the imgpath
    """
    # Use the true/false to index as 0 or 1
    chars = np.array([".","#"])[img.astype(int)]
    # to list of strings, including linebreaks
    content = ["".join(line) + "\n" for line in chars]
    # write to file
    with open(imagepath, "w") as file:
        file.writelines(content)

def measure_roughness():
    """
    Remove all black pixels that are part of monsters and count the remaining marks
    """
    # Load images
    image = get_image()
    monster = load_image(monsterpath)
    # remove all monsters
    sea = eliminate_with_transform(image, monster)
    # sum is count of black pixels
    return np.sum(sea)

def eliminate_with_transform(image, monster):
    """
    Try different transforms to eliminate monsters
    """
    for trans in range(8):
        # make copies because images are mutated
        transformed = transform(image.copy(), trans)
        sea, monsters = eliminate_monsters(transformed, monster)
        if monsters > 0:
            return sea
    


def eliminate_monsters(image, monster):
    """
    Find all places where there is a monster in the image and remove them.
    """
    # record number of monsters found
    eliminated = 0
    imgi, imgj = image.shape
    moni, monj = monster.shape
    # for all coords where a monster could fit
    for i in range(imgi - moni):
        for j in range(imgj - monj):
            # a window on the whole image of the size of the monster
            sample = image[i:i+moni, j:j+monj]
            # detect monster. Accept if in all cells where monster is true, sample is true
            contains_monster = np.all((sample == monster) | sample)
            # if so delete monster
            if contains_monster:
                # keep sample value but all true monster goes to false
                image[i:i+moni, j:j+monj] = sample & ~monster
                eliminated += 1
    return image, eliminated


print(measure_roughness())