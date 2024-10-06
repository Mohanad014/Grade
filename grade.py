import cv2
import pytesseract
import re
 
# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
# Load the image 
image = cv2.imread('10th_grade_sheet.jpg')
 
# Convert the image to grayscale  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(gray)

# Split the text into lines
lines = text.splitlines()
#print(lines)

# Define regular expression patterns
subject_score_pattern = r"(\w+)\s+([0-9]+)"
# name_pattern = r"Name\s*-\s*(.+)?"
# standard_pattern = r"Standard\s*-\s*(.+)?"
# total_pattern = r"Total\s*=\s*([0-9]+)"

# Initialize variables to store extracted information
name = None
standard = None
total = None

# Iterate through the lines and extract information
for line in lines:
    # Extract subject-score pairs
    match = re.search(subject_score_pattern, line)
    if match:
        subject = match.group(1)
        score = match.group(2)
        print(f"{subject}: {score}")

    # # Extract name
    # match = re.search(name_pattern, line)
    # print(match)
    # if match:
    #     name = match.group(1)

    # Extract standard
    # match = re.search(standard_pattern, line)
    # if match:
    #     standard = match.group(1)

    # # Extract total
    # match = re.search(total_pattern, line)
    # if match:
    #     total = match.group(1)

# Print the extracted name, standard, and total
# if name:
#     print(f"Name: {name}")
# if standard:
#     print(f"Standard: {standard}")
# if total:
#     print(f"Total: {total}")

# Display the image (optional, for debugging)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
