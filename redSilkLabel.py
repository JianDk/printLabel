#! /usr/bin/python
import os
from PIL import Image
import zpl
noPrint = 36

label = zpl.Label(160,40)
label.origin(35,20)
label.set_darkness(30)
label.write_graphic(Image.open('redSilkLabel.png'), width = 38)
label.endorigin()
printStr = bytes(label.dumpZPL(), encoding='utf8')

text_file = open("printLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()

printerName = 'Zebra_Technologies_ZTC_GX430t'

for i in range(noPrint):
    os.system(f"lp -o raw -d {printerName} printLabel.zpl")