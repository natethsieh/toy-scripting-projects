# Docs https://pillow.readthedocs.io/en/stable/

from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("blur.png", 'png') #png supports these image filters, whereas jpg might now

grey_scale = img.convert('L') # converts picture to greyscale 
grey_scale.save("grey.png", 'png')
grey_scale.show()
