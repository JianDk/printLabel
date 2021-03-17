import os
from PIL import Image
import zpl
numberPrint = input('Number of labels to print: ')
numberPrint = int(numberPrint)
label = zpl.Label(220,100)
label.origin(5,0)
label.set_darkness(30)
label.write_graphic(Image.open('/Users/jianxiongwu/Documents/Python/Github/printLabel/towGatherBoxLabel.png'), width = 100)
label.endorigin()
printStr = bytes(label.dumpZPL(), encoding='utf8')

text_file = open("printLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()
for i in range(numberPrint):
    os.system("lp -o raw printLabel.zpl")