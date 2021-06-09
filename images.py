from PIL import Image, ImageFilter

img = Image.open(r"C:\Users\so4re\Desktop\Applications\Programs\Images with Python\pikachu.jpg")
img_blur = img.convert('L')
resized = img_blur.resize((1080, 1080))

resized.save('grey.png', 'png')