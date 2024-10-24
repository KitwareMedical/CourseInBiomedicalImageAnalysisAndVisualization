import itk
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

im=itk.imread('data/CBCT-TextureInput.png', itk.F)
sobel=itk.sobel_edge_detection_image_filter(im)
arr = itk.array_from_image(sobel)

plt.subplot(1, 2, 1)
plt.gray()
plt.imshow(itk.array_view_from_image(im))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.gray()
plt.imshow(arr)
plt.axis('off')
