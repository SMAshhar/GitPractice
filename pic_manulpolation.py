import scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
f = misc.face()
imageio.imsave('abc.png', f)

plt.imshow(f)
plt.show()

# import numpy as np
# arr1 = np.ones((10,10))
# print(arr1)
# arr1[1:-1, 1::2] = 0
# print(arr1)

