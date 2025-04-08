# Python Photo Manipulation Toolkit

A mini image processing toolkit built using Python and the Pillow (`PIL`) library, capable of performing a variety of photo manipulation techniques including flipping, grayscale conversion, pixelation, color quantization, and Gaussian blur.

## Features

- **Horizontal & Vertical Flip**  
  Mirrors the image along the horizontal or vertical axis.

- **Grayscale Conversion**  
  Converts the image to grayscale using the average intensity of RGB values.

- **Color Quantization**  
  Reduces the number of colors in the image using a custom color palette and Euclidean distance-based matching.

- **Gaussian Blur**  
  Applies a blur effect by averaging neighboring pixels within a given radius.

- **Pixelation**  
  Groups pixels into square blocks and replaces each with a single color, creating a pixelated effect.

## 🧪 How to Use

1. Replace the `filename` variable with the name of the image file you'd like to test (default is `mario.jpg`).
2. Each function takes a copy of the original image and saves the result as a new file:
   - `horizontalflip.jpg`
   - `verticalflip.jpg`
   - `grayscale.jpg`
   - `colourquantization.jpg`
   - `gaussianblur.jpg`
   - `pixelate.jpg`

```python
filename = "your_image.jpg"
img = Image.open(filename)

horizontalFlip(img.copy())
verticalFlip(img.copy())
grayscale(img.copy())
colourQuantization(img.copy(), CL)
gaussianBlur(img.copy(), 3)
pixelate(img.copy(), 4)
