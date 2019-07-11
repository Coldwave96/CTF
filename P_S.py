from PIL import Image, ImageDraw
import sys

im = Image.new("RGB", (280, 280), "white")
draw = ImageDraw.Draw(im)

with open("Paint&Scan.txt", 'r') as f:
		while True:
			line = f.readline()
			#print line
			if not line:
				break
			exec 'draw.point(' + line + ', fill = (0, 0, 0))'
			#print 'draw.point(' + line + ', fill = (0, 0, 0))'
im.show()