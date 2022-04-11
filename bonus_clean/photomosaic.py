"""This program takes as a target image
4  most common sizes:
1080:1920, 1080:1350, 1080:1080, 1080:566"""

import os.path

from PIL import Image, ImageChops, ImageStat


def choose_best_image(main_image: Image, images: list):
    pics_diff = {}
    for image in images:
        # Generate diff image in memory.
        diff_img = ImageChops.difference(main_image, image)
        # Calculate difference as a ratio.
        stat = ImageStat.Stat(diff_img)
        diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
        pics_diff[diff_ratio] = image
    return pics_diff[min(pics_diff.keys())]


target = 'target_pic'
images_path = 'i_path'
images = ['1', '2', '3', '4', '5', '6']
target_image = Image.open(target)

imgwidth, imgheight = target_image.size
if imgheight == 566:
    target_image.resize((imgwidth, 560))
if imgheight == 1350:
    target_image.resize((imgwidth, 1340))

step = 20
resized_images =[]

for image in images:
    im = Image.open(os.path.join(images_path, image))
    im = im.resize((step, step))
    resized_images.append(im)


for i in range(0, imgwidth, step):
    for j in range(0, imgheight, step):
        compared_image = target_image.crop((i, j, i+step, j+step))
        inserted_image = choose_best_image(compared_image, resized_images)
        target_image.paste(inserted_image, (i, j))

target_image.save('image_mosaic.jpg')

