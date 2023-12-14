import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('Pictures/frame0.jpg')
# reading in an imageimage = mpimg.imread('solidWhiteCurve.jpg')# printing out some stats and plotting the imageprint('This image is:', type(image), 'with dimensions:', image.shape)


