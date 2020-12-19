import os
from PIL import Image
import zpl

label = zpl.Label(220,100)
label.origin(35,20)
label.set_darkness(30)
label.write_graphic(Image.open('FamilyBox.png'), width = 38)
label.endorigin()
printStr = bytes(label.dumpZPL(), encoding='utf8')

text_file = open("printLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()