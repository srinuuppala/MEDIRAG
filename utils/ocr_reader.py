import pytesseract
from PIL import Image

def read_image(path):

    image = Image.open(path)

    text = pytesseract.image_to_string(image)

    return text