# demo.py
from src.hybrid import create_hybrid_image
from resources import cat, dog

# Create a hybrid image
hybrid_image = create_hybrid_image(cat, dog, 1, 3, 'low', 1, 3, 'high', 0.5)

# Save the hybrid image
cv2.imwrite('resources/hybrid.png', hybrid_image)