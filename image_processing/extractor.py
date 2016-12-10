from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[1]
print("Will use lang '%s'" % (lang))

with open('data0.txt', 'a') as f:
    for i in range(200):
        image_file = 'images/image{}.png'.format(i)
        txt = tool.image_to_string(
            Image.open(image_file),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        f.write(txt)
        print(txt)
        f.write("\n______________\n")
