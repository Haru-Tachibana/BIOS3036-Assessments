from ij.gui import NewImage
from ij import IJ
import math  # need to use sqrt function to calculate the magnitude

lake_grayscale = IJ.getImage()  # get the grayscale image
processor = lake_grayscale.getProcessor()  # get the pixels

# get the width and height of the image
w = processor.getWidth()
h = processor.getHeight()

# create an output image for the edge magnitude - it's important to keep the input image safe.
output = NewImage.createImage("Sobel Edges Detection", w, h, 1, 8, NewImage.FILL_BLACK)
output_processor = output.getProcessor()  # get output pixels

# define 3*3 Sobel kernels as instructed for x and y directions
# x direction
sobel_x = [[1, 0, -1],
            [2, 0, -2],
            [1, 0, -1]]

# y direction
sobel_y = [[1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]]

# loop over the pixels while avoiding the borders
for x in range(1, w - 1):
    for y in range(1, h - 1):

        # apply sobel x and sobel y kernels
        gradient_x = 0
        gradient_y = 0

        for a in range(-1, 2):
            for b in range(-1, 2):
                pixel_value = processor.getPixel(x + a, y + b)
                gradient_x += pixel_value * sobel_x[a + 1][b + 1]
                gradient_y += pixel_value * sobel_y[a + 1][b + 1]

        # calculate the magnitude of the gradient to combine the outputs
        magnitude = math.sqrt(gradient_x ** 2 + gradient_y ** 2)

        # ensures no pixel value exceeds 255, keeping the image compatible with 8-bit grayscale standards (0 to 255)
        magnitude_norm = min(int(magnitude), 255)
        output_processor.putPixel(x, y, magnitude_norm)


# define 3 locations
locations_coor = [(28, 26), (116, 79), (128, 146)]

# loop over the specified locations and print the magnitude values
for loc in locations_coor:
    x, y = loc
    # ensure not exceed the boundaries
    if 1 <= x < w - 1 and 1 <= y < h - 1:
    	gradient_x = 0
        gradient_y = 0

        for a in range(-1, 2):
            for b in range(-1, 2):
                pixel_value = processor.getPixel(x + a, y + b)
                gradient_x += pixel_value * sobel_x[a + 1][b + 1]
                gradient_y += pixel_value * sobel_y[a + 1][b + 1]

        # Calculate the magnitude
        magnitude = math.sqrt(gradient_x ** 2 + gradient_y ** 2)
        magnitude_norm = min(int(magnitude), 255)

        print("the magnitude at ({}, {}): {}".format(x, y, magnitude_norm))

output.show()
