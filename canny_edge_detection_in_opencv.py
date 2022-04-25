import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/daram/GY642Files/subsetTifs/s2_july_tci.tif", 0)

# threshold values in Canny function
# manually tested to find threshold values
canny = cv2.Canny(img, 18, 70)

# writing output image - this raster could further processed in a GIS
#cv2.imwrite(r"C:\Users\daram\GY642Files\Project\Results\canny_s2_july_tci_3090.tif", canny)

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()
