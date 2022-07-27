1.	IMPORTS
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

2.	READING
image=Image.open("image.jpeg")

3.	DISPLAYING
image.show()
plt.imshow(image)

4.	PROPERTIES OF IMAGE
print(image.size)
print(image.format)
print(image.mode)

5.	SAVING
image.save("newimage.jpg")

6.	CROPPING
left=100
top=150
right=600
bottom=430
crop_image=image.crop((left,top,right,bottom))
plt.imshow(crop_image)

7.	COPYING
copied_image=image.copy()
plt.imshow(copied_image) 

8.	TRANSPOSING
transpose_image1=image.transpose(Image.FLIP_LEFT_RIGHT)
transpose_image2=image.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image3=image.transpose(Image.ROTATE_90)
transpose_image4=image.transpose(Image.TRANSPOSE)
plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(transpose_image1)
plt.title("FLIP_LEFT_RIGHT")
plt.subplot(3,2,2)
plt.imshow(transpose_image2)
plt.title("FLIP_TOP_BOTTOM")
plt.subplot(3,2,3)
plt.imshow(transpose_image3)
plt.title("ROTATE_90")
plt.subplot(3,2,4)
plt.imshow(transpose_image4)
plt.title("TRANSPOSE")

 
9.	RESIZING
newsize=(300,300)
plt.figure(figsize=(10,10))

resized_im1=image.resize(newsize,Image.BILINEAR)
resized_im2=image.resize(newsize,Image.BICUBIC)
resized_im3=image.resize(newsize,Image.LANCZOS)
plt.subplot(3,2,1)
plt.imshow(resized_im1)
plt.title("BILINEAR")
plt.subplot(3,2,2)
plt.imshow(resized_im2)
plt.title("BICUBIC")
plt.subplot(3,2,3)
plt.imshow(resized_im3)
plt.title("LANCZOS")

 
10.	ROTATING
angle=30
rotated_image=image.rotate(angle)
plt.imshow(rotated_image)

angle=-30
rotated_image=image.rotate(angle)
plt.imshow(rotated_image)

11.	TEXT WATERMARK
from PIL import ImageFont
from PIL import ImageDraw
watermarked_image=image.copy()
draw=ImageDraw.Draw(watermarked_image)
font=ImageFont.truetype("arial.ttf",200)
draw.text((0,0),"PYTHON",(1200,1200,1200),font=font)
plt.imshow(watermarked_image)
 
12.	IMAGE COLOUR FORMAT
bw_image=image.convert('L')
plt.imshow(bw_image,cmap='gray')

13.IMAGE ENHANCEMENT
from PIL import ImageEnhance
plt.figure(figsize=(10,10))
image_color_enhance= image.copy()
image1=ImageEnhance.Color(image_color_enhance).enhance(2.5)
image2=ImageEnhance.Contrast(image_color_enhance).enhance(2.5)
image3=ImageEnhance.Brightness(image_color_enhance).enhance(1.5)
image4=ImageEnhance.Sharpness(image_color_enhance).enhance(2.5)
plt.subplot(2,2,1)
plt.imshow(image1)
plt.title("Color")
plt.subplot(2,2,2)
plt.imshow(image2)
plt.title("Contrast")
plt.subplot(2,2,3)
plt.imshow(image3)
plt.title("Brigthness")
plt.subplot(2,2,4)
plt.imshow(image4)
plt.title("Sharpness")
 
14.ALPHA BENDING
image1=image.copy()
image2=image2.copy()
image2=image2.resize(image.size)
image_blend=Image.blend(image1,image2,0.5)
plt.imshow(image_blend)

15.IMAGE TRANSFORMATION
image_transform= image.copy()
image_transform=image_transform.transform(image_transform.size, Image.EXTENT,(100,100,image_transform.size[0],image_transform.size[1]//2))
plt.imshow(image_transform)

16.FLIPPING CHANNELS
image_channels=image.copy()
b, g, r= image_channels.split()
im= Image.merge("RGB",(b, g, r))
plt.imshow(im)

 

