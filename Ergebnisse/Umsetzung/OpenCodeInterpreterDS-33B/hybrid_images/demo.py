import cv2
import numpy as np
from src.hybrid import create_hybrid_image

# Load images
img1 = cv2.imread('resources/cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('resources/dog.jpg', cv2.IMREAD_GRAYSCALE)

# Create hybrid image
hybrid_img = create_hybrid_image(img1, img2, 5, 11, 'low', 5, 11, 'high', 0.5)

# Save hybrid image
cv2.imwrite('resources/hybrid.png', hybrid_img)