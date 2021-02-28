import numpy as np
import pywt  # py wavelet transform library
import cv2


def w2d(img, mode='haar', level=1):
    imArray = img
    # Datatype conversions
    # convert to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
    # convert float
    imArray = np.float32(imArray)
    imArray /= 255;
    # compute co-efficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process co-efficinets
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H

