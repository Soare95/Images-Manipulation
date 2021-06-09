from PIL import Image, ImageFilter

img = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Images with Python\mountain.jpg')
img.thumbnail((400, 400))
img.save('mountain1.jpg')

print(img.size)