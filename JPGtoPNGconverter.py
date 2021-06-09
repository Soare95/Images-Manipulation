import sys
import os
from PIL import Image

#grab the 2 arguments from cmd
images_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new folder exists, if not create a new one
if not os.path.exists(output_folder):
	os.mkdir(output_folder)

#loop through folder
#convert each image into png
#save the images
for filename in os.listdir(images_folder):
	img = Image.open(f'{images_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')
