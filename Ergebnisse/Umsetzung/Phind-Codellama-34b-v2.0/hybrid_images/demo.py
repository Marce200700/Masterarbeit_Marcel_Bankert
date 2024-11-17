from src.hybrid import create_hybrid_image
import cv2

def main():
    img1 = cv2.imread('resources/cat.jpg')
    img2 = cv2.imread('resources/dog.jpg')

    hybrid_img = create_hybrid_image(img1, img2, 10, 5, 'high', 10, 5, 'low', 0.5)

    cv2.imwrite('resources/hybrid.png', hybrid_img)

if __name__ == "__main__":
    main()