import random
from io import BytesIO

import pokebase as pb
from PIL import Image

from utils import crop_image

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
