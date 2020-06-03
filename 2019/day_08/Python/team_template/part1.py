import numpy as np
from pathlib import Path

from load_input import get_input


def get_layers(image_data, layer_size):
    layers = []
    for starting_index in range(0, len(image_data), layer_size):
        layers.append(image_data[starting_index: starting_index + layer_size])

    return layers


def meaningless_calculation(image_data, width, height):
    layer_size = width * height
    layers = get_layers(image_data, layer_size)
    zero_count = layer_size
    zero_index = 0
    for index, layer in enumerate(layers):
        if layer.count('0') < zero_count:
            zero_count = layer.count('0')
            zero_index = index
    fewest_zeros_layer = layers[zero_index]
    return fewest_zeros_layer.count('1') * fewest_zeros_layer.count('2')


def decode_image_using_numpy(image_data, width, height):
    image_data = image_data.reshape((-1, height, width))
    final_image = image_data[0].copy()
    number_of_layers = image_data.shape[0]
    # So what's going on here?  At this point, we have a 3D array: (depth,
    # height, width).  This loop is looping over each depth layer:
    for index in range(number_of_layers):
        final_image[final_image == 2] = image_data[index][final_image == 2]
        # And this is where the work happens.  Let's break it into pieces:
        #
        # Both sides: [final_image==2] - creates a 2D boolean array of
        # (height, width), with values of True where final_image==2, False
        # everywhere else.  Note this is regenerated for each layer.  I'm
        # deliberately avoiding the term "mask" here - a mask has a particular
        # meaning in numpy.
        #
        # LHS: final_image[final_image==2] - this selects only those pixels in
        # the final_image that still have value of 2 (i.e. those that are
        # still transparent).
        #
        # RHS part 1: image_data[index] - this slices the current 2D layer out
        # of the 3D image_data.  This 2D layer is the same shape as the final
        # image (since each layer is the same shape).
        #
        # RHS part2: image_data[index][final_image==2] - and this selects the
        # values in *the layer* where the *final_image* is still transparent,
        # relying on them both being the same shape.
        #
        # Possibly less opaque version:
        # current_layer = image_data[index]
        # final_image[final_image == 2] = current_layer[final_image == 2]
    return final_image


def decode_image(image_data, width, height):
    layer_size = width * height
    layers = get_layers(image_data, layer_size)
    final_image = []
    for index in range(layer_size):
        for layer in layers:
            if layer[index] != '2':
                final_image.append(layer[index])
                break

    for index in range(layer_size, 1, -width):
        final_image.insert(index, '\n')
    return ''.join(final_image).strip()


def part1():
    input_ = get_input()
    return meaningless_calculation(input_, 25, 6)


def part2():
    input_ = get_input()
    return decode_image(input_, 25, 6).replace('0', ' ')


def part2_using_numpy():
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    array = np.genfromtxt(input_file, delimiter=1, dtype=np.int32)
    return np.array_str(
        decode_image_using_numpy(array, 25, 6)).replace('0', ' ').replace(
        '[', ' ').replace(']', ' ')


if __name__ == "__main__":
    print(f'Part 1:\n{part1()}')
    print(f'Part 2:\n{part2()}')
    print(f'Part 2 using NumPy:\n{part2_using_numpy()}')
