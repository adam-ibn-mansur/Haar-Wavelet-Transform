import numpy as np
import matplotlib.pyplot as pyplot

import pywt
import pywt.data

#load image
ogImage = pywt.data.camera()

#Wavelet transform of image, and plot approximation and details
titles = ['Approximation', 'Horizontal detail', 'Vertical detail', 'Diagonal detail']
coefficients = pywt.dwt2(ogImage, 'haar')

hwt_A, (hwt_HD, hwt_VD, hwt_DD) = coefficients
figure = plt.figure(figsize = (12, 3))
for i, a in enumerate([hwt_A, hwt_H, hwt_V, hwt_D]):
    hwt_X = fig.add_subplot(1, 4, i + 1)
    hwt_X.imshow(a, interpolation = 'nearest', cmap = plt.cm.gray)
    hwt_X.set_title(titles[i], fontsize=10)
    hwt_X.set_xticks([])
    hwt_X.set_yticks([])

fig.tight_layout()
plt.show()
