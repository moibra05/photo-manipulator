# Mohamed

import PIL, math
from PIL import Image

def horizontalFlip(img):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            # To horizontaly mirror a pixel's location its coordinates must be changed to 
            # (width - x - 1, y)
            xLoc = w - x - 1
            colour = (img.getpixel((x, y)))
            newImg.putpixel((xLoc, y), colour)
    newImg.save("horizontalflip.jpg", format = "jpeg")
    newImg.show()

def verticalFlip(img):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            # To vertically mirror a pixel's location its coordinates must be changed to 
            # (x, height - y - 1)
            yLoc = h - y - 1
            colour = (img.getpixel((x, y)))
            newImg.putpixel((x, yLoc), colour)
    newImg.save("verticalflip.jpg", format = "jpeg")
    newImg.show()

def grayscale(img):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            totalColour = 0
            colourVals = img.getpixel((x, y))
            # Takes the average of each pixel's total colour value and sets that as the new value
            # for R, G, and B in (R, G, B)
            for colour in colourVals:
                totalColour += colour
                average = totalColour // 3
            newImg.putpixel((x, y), (average, average, average))
    newImg.save("grayscale.jpg", format = "jpeg")
    newImg.show()

def colourQuantization(img, CL):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            (r, g, b) = img.getpixel((x, y))
            results = []
            for subset in CL:
                # Euclidean distance formula to find the minimal distance between points with 
                # three dimensions: sqrt((r1 - r2)^2 + (g1 - g2)^2 + (b1 - b2)^2)
                results.append(math.sqrt((r - subset[0])**2 + (g - subset[1])**2 + (b - subset[2])**2))
            # Compares the distance of each pixel to every subset and takes the index of the lowest
            # distance to a particular subset to match its pixel colour value to its respective index
            minDistanceIndex = results.index(min(results))
            newColour = CL[minDistanceIndex]
            newImg.putpixel((x, y), (newColour))
    newImg.save("colourquantization.jpg", format = "jpeg")
    newImg.show()

def gaussianBlur(img, rad):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    for row in range(w):
        for col in range(h):
            # Empty 2D List to store the RGB values of each pixel within the radius
            colours = [[],[],[]]
            totR = 0
            totG = 0
            totB = 0
            # Another pair of for loops to separately iterate through the pixels existing in the 
            # square of radius 'rad' with (row, col) being in the centre
            for x in range(row - rad, row + rad + 1): 
                for y in range(col - rad, col + rad + 1):
                    # If statement to check that the values of the pixel coordinates exist within 
                    # the image's range
                    if x >= 0 and y >= 0 and x < w and y < h:
                        (r, g, b) = img.getpixel((x, y))
                        colours[0].append(r)
                        colours[1].append(g)
                        colours[2].append(b)
                    else:
                        continue
            # Calculates the average of RGB using the surrounding pixels
            for r in colours[0]:
                totR += r
            for g in colours[1]:
                totG += g
            for b in colours[2]:
                totB += b
            avgRGB = (totR // len(colours[0]), totG // len(colours[1]), totB // len(colours[2]))
            newImg.putpixel((row, col),(avgRGB))
    newImg.save("gaussianblur.jpg", format = "jpeg")
    newImg.show()

def pixelate(img, threshold):
    (w, h) = img.size
    newImg = Image.new("RGB", (w, h))
    # Groups pixels in a "threshold" x "threshold" pattern
    for groupRow in range(0, w, threshold):
        for groupCol in range(0, h, threshold):
            # Sets the colour of the top left pixel to a variable for all the pixels in the group to change to
            # then iterates through each pixel in the group to change its colour
            newGroupColour = img.getpixel((groupRow, groupCol))
            for x in range(threshold): 
                for y in range(threshold):
                    try:
                        # Pixel group location is determined by adding the group row/column to the respective
                        # x/y position and setting all those pixels in the group to the same colour
                        newImg.putpixel((x + groupRow, y + groupCol), (newGroupColour))
                    except Exception:
                        continue
    newImg.save("pixelate.jpg", format = "jpeg")
    newImg.show()

#change the file name if you want to test your own image
filename = "mario.jpg"
img = Image.open(filename)

horizontalFlip(img.copy()) #DO NOT MODIFY FUNCTION CALL
verticalFlip(img.copy()) #DO NOT MODIFY FUNCTION CALL
grayscale(img.copy()) #DO NOT MODIFY FUNCTION CALL

'''
Colour Quantization
CL stands for colour list. I've provided some examples below, but you should also test with your
own list of colour tuples.
'''
#CL = [(0, 0, 0), (255, 255, 255)]
#CL = [(0,0,0), (0,0,50), (0,0,100), (0,0,150), (0,0,200), (0,0,250)]
CL = [(249, 228, 177), (17, 51, 75), (196, 51, 47), (122, 149, 158)]
#CL = [(45,70,82),(79,155,143),(228,196,119),(233,165,108),(217,117,89)]

colourQuantization(img.copy(), CL) #DO NOT MODIFY FUNCTION CALL
gaussianBlur(img.copy(), 3) #DO NOT MODIFY FUNCTION CALL
pixelate(img.copy(), 4) #DO NOT MODIFY FUNCTION CALL