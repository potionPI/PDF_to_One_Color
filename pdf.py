# conda create -n pdf_env python=3.11
# conda activate pdf_env
# brew install poppler
# pip install pdf2image 
# pip install Pillow

# cd /Users/cynthiawu/Downloads
# python pdf.py

from pdf2image import convert_from_path
from IPython.display import display, Image
from PIL import Image, ImageOps

MY_NEW_COLOR = "red";
pdf_filename = 'pdf_long.pdf'
images = convert_from_path(pdf_filename)
new_images = []

for i in range(len(images)):

    curr_img = images[i]
    curr_img = ImageOps.grayscale(curr_img)
    curr_img = ImageOps.colorize(curr_img, black=MY_NEW_COLOR, white="white")

    new_images.append(curr_img)

new_images[0].save("out_" + MY_NEW_COLOR + ".pdf", save_all=True, append_images=new_images[1:])