import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Importing image data into Numpy array
img= mpimg.imread('photo-me-gallery-photography-theme.jpg')

#Plotting numpy arrays as image
imgplot = plt.imshow(img)

# Applying pseudocolor schemes to image plots
lum_img = img[:,:,0]
plt.imshow(lum_img)




fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

for c, ax in zip(range(3), axs):
    tmp_im = np.zeros(img.shape, dtype="uint8")
    tmp_im[:,:,c] = img[:,:,c]
    ax.imshow(tmp_im)
    ax.set_axis_off()
plt.show()



# Making image in black and white
plt.imshow(lum_img, cmap="gray", vmin =20, vmax=100)

plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

imgplot = plt.imshow(lum_img, clim=(0.2, 0.7))
