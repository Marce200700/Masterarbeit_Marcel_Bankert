import cv2
from src.hybrid import create_hybrid_image

# Load images
img1 = cv2.imread('resources/cat.jpg')
img2 = cv2.imread('resources/dog.jpg')

# Create hybrid image
hybrid_img = create_hybrid_image(img1, img2, 10, 31, 'low', 10, 31, 'high', 0.5)

# Save hybrid image
cv2.imwrite('resources/hybrid.png', hybrid_img)