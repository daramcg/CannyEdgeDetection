import matplotlib.pyplot as plt
import cv2
print('VX Public Number: Orange code / juzicode.com')
print('cv2.__version__:',cv2.__version__)
plt.rc('font',family='Youyuan',size='9')

img_src = cv2.imread(r"C:\Users\daram\GY642Files\Project\QGIS_TCI_summer.tif", cv2.IMREAD_GRAYSCALE)
grad_x = cv2.Scharr(img_src,cv2.CV_16S,1,0)
grad_y = cv2.Scharr(img_src,cv2.CV_16S,0,1)
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv2.imwrite(r"C:\Users\daram\gY642Files\Results\output_scharrCombinedSUMMER.tif", grad)

fig,ax = plt.subplots(2,2)
ax[0,0].set_title('Original Map')
ax[0,0].imshow(img_src ,cmap = 'gray')
ax[0,1].set_title('abs_grad_x')
ax[0,1].imshow(abs_grad_x,cmap = 'gray')
ax[1,0].set_title('abs_grad_y')
ax[1,0].imshow(abs_grad_y,cmap = 'gray')
ax[1,1].set_title('grad-x+y')
ax[1,1].imshow(grad,cmap = 'gray')
ax[0,0].axis('off');ax[0,1].axis('off');ax[1,0].axis('off');ax[1,1].axis('off')
plt.show()