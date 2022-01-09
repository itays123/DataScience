# Exercise 10 - binary pictures to colored image and binary image to black and white image
import numpy as np
import matplotlib.pyplot as plt

MAX_RGB_VALUE=255

def picture_to_mono(picture=np.zeros((100,100,3))):
    red = picture[:, :, 0]
    green = picture[:, :, 1]
    blue = picture[:, :, 2]
    average = (red + green + blue) / 3
    return average

def picture_to_binary(picture=np.zeros((100, 100, 3))):
    result = picture_to_mono(picture)
    result /= MAX_RGB_VALUE # now all variables are between 0 and 1
    result = np.round(result)
    return result


picture = np.zeros((100, 100, 3))
picture[0:50, 0:50, 0] = 255 # Set red to 255 in those indexes 
picture[50:100, 0:50, 1] = 255 # Set green to 255 in those indexes
picture[0:50, 50:100, 2] = 255 # Set blue to 255 in those indexes
picture[50:100, 50:100, :] = 255 # Set everything to 255 in those indexes
print(picture_to_mono(picture))
print(picture_to_binary(picture))