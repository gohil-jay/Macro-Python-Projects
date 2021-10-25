"""
Modules to install:

!pip install pyqrcode
!pip install pypng
"""

import pyqrcode

link = 'https://jay-gohil.me/'
url =  pyqrcode.create(link)

url.svg('QR.svg', scale=20)
print(url.terminal(quiet_zone=1))
