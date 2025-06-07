'''Image Brightness and Edge Detection using NumPy'''

import numpy as np
import matplotlib.pyplot as plt

#Here we are simulating a greysacale image of 8x8 pixels , Here value ranges from 0 to 255
image = np.random.randint(0,256, (8,8))
print("Original Image:\n", image)

#Here we are increasing the image brightness using vectorized operations
bright_image = image + 50
bright_image = np.clip(bright_image, 0 , 255) #here by using 255 we are ensuring that Image remains in the scale limits 0-255
# by using .clip operation we are ensuring that image values stay in 0-255 limits
print("\n Brightened image : \n ", bright_image)

#Proceeding on to edge detection using sobel kernel and here we are using vertical edge detection 
sobel_kernel = np.arrray([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

#A function to apply kernel
def apply_convolution(img, kernel):
    output = np.zeros((img.shape[0] -2 , img.shape[1]-2))
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            region = img[i: i+3, j: j+3]
            output[i,j]= np.sum(region *kernel)
    return output

edges = apply_convolution(image, sobel_kernel)
print("\n Edge Detected Image\n ", edges)

#FFT
fft_image = np.fft.fft2(image)
magnitude_spectrum = np.abs(fft_image)
print("\nFFT Magnitude Spectrum:\n", magnitude_spectrum)

#Visualizations of the image


