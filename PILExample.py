from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

#img = Image.open("background.png")
namedata = "Akın"

bottom = Image.open("background.png")
draw = ImageDraw.Draw(bottom)
print(draw.im.size[0])
sizef = 100
canvas_width = 400
canvas_height = 400
img_center = (canvas_width/2, canvas_height/2)
img = Image.new('RGB', (canvas_width, canvas_height), (0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('YoungSerif-Regular.otf', sizef)
#draw.text(img_center, 'Text', fill='#1764b2' , font=font)
#draw.rectangle(img.getbbox())



#font = ImageFont.truetype("YoungSerif-Regular.otf", sizef, encoding="utf-8")
heightf = font.getsize(namedata)[1]
widthf = font.getsize(namedata)[0]
#img = Image.new('RGBA', (widthf, heightf), (0, 0, 0, 0))
# ----------RESIZING----------------------
while heightf <400:
    sizef += 1
    font = ImageFont.truetype("YoungSerif-Regular.otf", sizef, encoding="utf-8")
    heightf = font.getsize(namedata)[1]
widthf = font.getsize(namedata)[0]
print(str(widthf) + "," + str(heightf))
if widthf > 2000:
    sizef = 200
    font = ImageFont.truetype("YoungSerif-Regular.otf", sizef, encoding="utf-8")
    widthf = font.getsize(namedata)[0]
    heightf = font.getsize(namedata)[1]
#---------------------------------------------
print(str(widthf) + "," + str(heightf))
draw.text((2048-widthf, 1024-heightf/2),namedata,font=font, fill='#1764b2',anchor='mm')
#draw.rectangle(img.getbbox())
draw = ImageDraw.Draw(img)
print('Text at: ', img.getbbox())
bottom.save('sample-out2.png')
img.save("hey.png")
