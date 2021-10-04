from PIL import Image
from utils import cropImage
from io import BytesIO
import random
import pokebase as pb

block = '██'

TOTAL_POKEMON = 898

pokemon = pb.SpriteResource('pokemon', random.randint(1, TOTAL_POKEMON))
image = Image.open(BytesIO(pokemon.img_data)).convert('RGBA')

cropped = cropImage(image)

length, width, _ = cropped.shape
for y in range(length):
    for x in range(width):
        # get RGBA value,
        r, g, b, a = cropped[y, x, :]

        # if transparant print [SPACE] ' '
        if a == 0:
            print('  ', end='')

        # print colored block
        else:
            print('\x1b[38;2;{};{};{}m'.format(r, g, b) + block, end='')
    print()
