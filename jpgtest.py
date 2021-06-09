import sys
import os
from PIL import Image

#create 2 arguments for the folder
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new exists, if not, create a new folder
if not os.path.exists(output_folder):
	os.mkdir(output_folder)

#open the images
#convert the images
#save the images
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')