import cv2
import argparse
import re
import os
from scipy import ndimage
import pytesseract

# Set Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\62086\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Function to detect orientation and rotate the image
def rotate(image):
    try:
        angle = int(re.search(r'(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
        rotated = ndimage.rotate(image, float(angle) * -1)
        return rotated
    except Exception as e:
        print("Rotation Error:", e)
        return image

# Preprocessing function
def preprocessing(image):
    w, h = image.shape[:2]
    if w < h:
        image = rotate(image)
    resized_image = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
    grey_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.medianBlur(grey_image, 3)
    thres_image = cv2.adaptiveThreshold(blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 13, 7)
    return thres_image, resized_image

# Function to mask first 8 digits of the Aadhar number
def aadhar_mask_and_ocr(thres_image, resized_image):
    d = pytesseract.image_to_data(thres_image, output_type=pytesseract.Output.DICT)
    number_pattern = r"(?<!\d)\d{4}(?!\d)"
    n_boxes = len(d['text'])
    c = 0
    temp = []
    UID = []

    final_image = resized_image.copy()
    
    for i in range(n_boxes):
        if int(d['conf'][i]) > 20 and re.match(number_pattern, d['text'][i]):
            if c < 2:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 255, 255), -1)
                temp.append(d['text'][i])
                c += 1
            elif c >= 2 and d['text'][i] in temp:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 255, 255), -1)
            elif c == 2:
                UID = temp + [d['text'][i]]
                c += 1

    final_image = cv2.resize(final_image, None, fx=0.33, fy=0.33)
    return final_image, UID

# Main function to process all images in a folder
def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"Error loading image {filename}")
                continue

            print(f"Processing {filename}...")

            thres_image, resized_image = preprocessing(image)
            masked_image, UID = aadhar_mask_and_ocr(thres_image, resized_image)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, masked_image)
            print(f"Saved masked image: {output_path}")

# Command-line argument parsing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_folder", required=True, help="Path to the folder containing images")
ap.add_argument("-o", "--output_folder", required=True, help="Path to the folder where masked images will be saved")
args = vars(ap.parse_args())

# Run the process
process_folder(args["input_folder"], args["output_folder"])
