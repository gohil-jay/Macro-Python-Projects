"""
Modules to install: pyqrcode
!pip install pyqrcode
"""

import pyqrcode

link = 'https://jay-gohil.me/'
url =  pyqrcode.create(link)

url.svg('QR.svg', scale=10)
print(url.terminal(quiet_zone=1))
