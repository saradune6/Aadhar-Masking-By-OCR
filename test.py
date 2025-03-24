import cv2

image_path = "C:/Users/62086/Downloads/aadhar-mask-ocr-main/aadhar-mask-ocr-main/images/img3.png"
image = cv2.imread(image_path)


if image is None:
    print("Image not found or unreadable! Check the file path or format.")
else:
    print("Image loaded successfully!")
    cv2.imshow("Test Image", image)  # Opens the image in a window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
