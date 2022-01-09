# Exercise 11 - build an image
import numpy as np
import matplotlib.pyplot as plt

MAX_RGB_VALUE=255
RED_INDEX=0
BLUE_INDEX=2

picture = np.zeros((100, 200, 3), dtype=np.uint8)

# Set red border
picture[0:25, 0:100, RED_INDEX] = MAX_RGB_VALUE
picture[75:100, 0:100, RED_INDEX] = MAX_RGB_VALUE
picture[0:100, 0:25, RED_INDEX] = MAX_RGB_VALUE
picture[0:100, 75:100, RED_INDEX] = MAX_RGB_VALUE

# Set blue border (indentical method)
picture[0:25, 100:200, BLUE_INDEX] = MAX_RGB_VALUE
picture[75:100, 100:200, BLUE_INDEX] = MAX_RGB_VALUE
picture[0:100, 100:125, BLUE_INDEX] = MAX_RGB_VALUE
picture[0:100, 175:200, BLUE_INDEX] = MAX_RGB_VALUE

# Set inner blue and inner red
picture[25:75, 25:75, BLUE_INDEX] = MAX_RGB_VALUE
picture[25:75, 125:175, RED_INDEX] = MAX_RGB_VALUE

# Show image
plt.imshow(picture)
plt.show()