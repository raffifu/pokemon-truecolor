import random
from io import BytesIO

import pokebase as pb
from PIL import Image

import numpy as np


def crop_image(image):
    arr = np.array(image)
    return arr[np.ix_(arr[:, :, 3].any(1), arr[:, :, 3].any(0))]

def generate():
    BLOCK = '██'
    TOTAL_POKEMON = 898

    pokemon = pb.SpriteResource('pokemon', random.randint(1, TOTAL_POKEMON))
    image = Image.open(BytesIO(pokemon.img_data)).convert('RGBA')

    cropped_image = crop_image(image)

    length, width, _ = cropped_image.shape
    for y in range(length):
        for x in range(width):
            r, g, b, a = cropped_image[y, x, :]  # get RGBA value

            if a == 0:  # print whitespace if pixel is transparent (a == 0)
                print('  ', end='')
            else:  # print colored block
                print('\x1b[38;2;{};{};{}m'.format(r, g, b) + BLOCK, end='')

        print('\033[0m')  # reset text color
