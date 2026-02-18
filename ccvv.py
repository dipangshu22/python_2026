import cv2
import pytesseract

# If Windows, specify path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
img = cv2.imread("imag1.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold (improves OCR accuracy)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Detect text
text = pytesseract.image_to_string(thresh)

print("Detected Text:")
print(text)
a=open("text22.txt","w")
b=a.write(text)
print(b)


# Show image
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
