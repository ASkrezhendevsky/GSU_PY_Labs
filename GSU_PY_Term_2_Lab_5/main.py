from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import qrcode
import math
import os


def resize_to_MP(picture, pixel_amount):
    x = picture.size[0]
    y = picture.size[1]

    x_new = math.sqrt(pixel_amount / x * y)
    y_new = x_new / x * y

    target_size = (int(x_new), int(y_new))
    print(target_size)
    picture.resize(target_size)


output_image_path = "output/"
input_image_path = "input/"
author_image_name = "AuthorImage.jpg"
author_image_size = (100, 100)
target_pixel_amount = 2000000
author_tag_id = 315
date_tag_id = 306
text_color = (50, 50, 50)
font = ImageFont.truetype("arial.ttf", 250)

for directory, folder, files in os.walk(input_image_path):
    print(directory, folder, files)

image_names = files

author_photo = Image.open(author_image_name)
author_photo.resize(author_image_size)

for image in image_names:
    photo = Image.open(input_image_path + image)

    resize_to_MP(photo, target_pixel_amount)

    drawing = ImageDraw.Draw(photo)

    if photo.size[0] < photo.size[1]:
        drawing.rotate()

    photo_info = photo.getexif()
    print(photo_info)
    try:
        text = photo_info[author_tag_id]
    except:
        text = "none"
    try:
        text += photo_info[date_tag_id]
    except:
        text += "none"
    drawing.text((20, photo.size[1] * 0.9), text, fill=text_color, font=font)

    photo.paste(author_photo, (photo.size[1] - author_image_size[0], 0))

    qr = qrcode.make('test text')
    photo.paste(qr)

    print(output_image_path + image)
    photo.save(output_image_path + image)
