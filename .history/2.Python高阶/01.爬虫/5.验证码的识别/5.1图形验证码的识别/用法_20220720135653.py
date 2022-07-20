from email.mime import image
from msilib.schema import tables
import pytesseract
from PIL import Image
import requests

re = requests.get('http://my.cnki.net/elibregister/CheckCode.aspx')
with open(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg',
        'wb') as f:
    f.write(re.content)

image = Image.open(
    r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg'
)
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
