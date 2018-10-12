from pyzbar.pyzbar import decode
from PIL import Image

data = decode(Image.open('QR_Code.png'))
code = data[0][0]

print("result is ", code)