import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
image_path=r""
img=Image.open(image_path)
text=pytesseract.image_to_string(img)
print("extracted text")
print(text)
