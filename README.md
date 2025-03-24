# Aadhar Number Masking using OCR

This project uses **Tesseract OCR** and **OpenCV** to detect and mask the first 8 digits of an Aadhar number from images. It processes all images in a given folder and saves the masked images in a specified output folder.

## Features
- Detects Aadhar numbers in images using **Tesseract OCR**
- Masks the first 8 digits of the detected Aadhar number
- Supports batch processing of images in a folder
- Saves the processed images in an output directory

## Requirements
Ensure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)
- `pytesseract` (Tesseract OCR)
- `scipy`

### Install dependencies
```bash
pip install opencv-python pytesseract scipy
```

### Install Tesseract OCR
Download and install Tesseract OCR from:
[Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)

After installation, update the script with the correct path to `tesseract.exe`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\YourUsername\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
```

## Usage
### Run the script
```bash
python script.py -i "path/to/input_folder" -o "path/to/output_folder"
```

### Example
```bash
python script.py -i "images/" -o "masked_images/"
```

## How It Works
1. The script loops through all `.jpg`, `.jpeg`, and `.png` images in the `input_folder`.
2. It detects orientation and rotates the image if necessary.
3. Preprocesses the image (grayscale, blur, thresholding) for better OCR accuracy.
4. Uses **Tesseract OCR** to extract text and locate Aadhar numbers.
5. Masks the first 8 digits of the Aadhar number.
6. Saves the masked images in `output_folder`.

## Example Output
**Original Image:**
![Original](docs/img.png)

**Masked Image:**
![Masked](docs/img.png)

## License
This project is licensed under the MIT License.

## Contributions
Feel free to submit issues or pull requests to improve the script!

## Author
[Your Name] - [GitHub Profile](https://github.com/yourgithub)


# aadhar-mask-ocr

Python code to perform Masking on First 8 digits of Aadhar and also perform OCR to return UID
Packages used: Tesseract, OpenCV, Scipy

Usage:
`python aadhar_mask_ocr.py --image images/img1.jpeg`

Output:\
`Masked digits in given image. Displaying...`\



