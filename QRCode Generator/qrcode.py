import pyqrcode
import png
from pyqrcode import QRCode

s='''NAME:SURIYAKUMAR
LinkedIn: http://linkedin.com/in/suriyakumar-s-23961614a
Gmail:suryaten7@gmail.com'''
url=pyqrcode.create(s)
url.png("location.png",scale=25)
