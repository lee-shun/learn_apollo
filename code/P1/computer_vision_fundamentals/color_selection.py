import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read in the image and print out some stats
image = mpimg.imread('test.jpg')
print('This image is:',type(image),
      'with dimensions:',image.shape)

#Grab the x and y size and make a copy of the image
yszie  = image.shape[0]
xszie  = image.shape[1]

#Note: always make a copy rather than simply using "="
color_select = np.copy(image)


#define the threshold# Define our color selection criteria
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]


thresholds = (image[:,:,0] < rgb_threshold[0]) \
              |  (image[:,:,1] < rgb_threshold[1])  \
              |   (image[:,:,2] < rgb_threshold[2] )
color_select[thresholds] = [0,0,0]

#display
plt.imshow(color_select)
plt.show()
