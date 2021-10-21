import numpy as np


def crop_image(image):
    arr = np.array(image)
    return arr[np.ix_(arr[:, :, 3].any(1), arr[:, :, 3].any(0))]
