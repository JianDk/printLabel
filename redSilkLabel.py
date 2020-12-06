#! /usr/bin/python
import os
from PIL import Image
import zpl

label = zpl.Label(160,40)
label.origin(35,20)
label.set_darkness(30)
label.write_graphic(Image.open('label.png'), width = 38)
label.endorigin()
printStr = bytes(label.dumpZPL(), encoding='utf8')


text_file = open("printLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()

os.system("lp -o raw printLabel.zpl")