#Print both the text and logo labels for the dimsum box internal package
import os
from PIL import Image
import zpl
import time

labelLogo = zpl.Label(57,57)
labelLogo.origin(28,2)
labelLogo.set_darkness(30)
labelLogo.write_graphic(Image.open('top.png'), width = 50)
labelLogo.endorigin()
printStr = bytes(labelLogo.dumpZPL(), encoding='utf8')

text_file = open("printLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()

textLabel = ['Cucumber Salad',
'Pak Choi',
'Wok Noodle',
'Veg. Big Bao',
'Veg. Gaozi Boil',
'Veg. Gaozi Pan Fry']

labelText = zpl.Label(57,57)
labelText.origin(25,25)
labelText.write_text("Char Siu So", char_height=6, char_width=6, line_width=60, justification='C')
labelText.endorigin()
printStr = bytes(labelText.dumpZPL(), encoding='utf8')
text_file = open("textLabel.zpl", "wb")
text_file.write(printStr)
text_file.close()
nPrint = input('Number of prints : ')
for i in range(int(nPrint)):
    for item in textLabel:
        labelText = zpl.Label(57,57)
        labelText.origin(25,25)
        labelText.write_text(item, char_height=6, char_width=6, line_width=60, justification='C')
        labelText.endorigin()
        printStr = bytes(labelText.dumpZPL(), encoding='utf8')
        text_file = open("textLabel.zpl", "wb")
        text_file.write(printStr)
        text_file.close()

        os.system("lp -o raw printLabel.zpl")
        os.system("lp -o raw textLabel.zpl")
    
    time.sleep(10)