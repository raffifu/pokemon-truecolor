import numpy as np


def cropImage(image):
    arr = np.array(image)
    x, y, _ = arr.shape
    return arr[np.ix_(arr[:, :, 3].any(1), arr[:, :, 3].any(0))]
