import cv2
import numpy as np
import os

# Define the number of rows and columns for the mosaic
n_rows = 4
n_cols = 4

# Define the size of the images
image_size = (720, 720)

# Load the images from a directory
images_dir = "photos"
images = []
for filename in os.listdir(images_dir):
    img = cv2.imread(os.path.join(images_dir, filename))
    img = cv2.resize(img, image_size)
    images.append(img)

# Create the mosaic
mosaic = np.zeros((n_rows * image_size[0], n_cols * image_size[1], 3), dtype=np.uint8)

for i in range(n_rows):
    for j in range(n_cols):
        index = i * n_cols + j
        if index >= len(images):
            break
        img = images[-index]
        mosaic[i*image_size[0]:(i+1)*image_size[0], j*image_size[1]:(j+1)*image_size[1], :] = img

# Save the mosaic
cv2.imwrite("mosaic.jpg", mosaic)