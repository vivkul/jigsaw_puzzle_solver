import Image
import numpy as np
import sys


def merge_image(m,n,image_width, image_height):
	t=n*m
	merge_order=np.random.permutation(t)
	final_image=Image.new('RGB',(image_width,image_height))
	w_chunk=image_width/m
	h_chunk=image_height/n
	k=0
	img_ext=".jpg"
	order_txt=open('final.txt','a')
	for i in range(1,n+1):
		lt_h=h_chunk*(i-1)
		for j in range(1,m+1):
			lt_w=w_chunk*(j-1)
			order_txt.write(str(merge_order[k]+1))
			order_txt.write("\n")
			part_name=str(merge_order[k]+1)
			part_name+=img_ext
			part_im=Image.open(part_name)
			final_image.paste(part_im,(lt_w,lt_h))
			k=k+1
	final_image.save("final.jpg")

def split_image(im,m,n):
	w,h=im.size
	print w
	print h
	w_chunk=w/m
	h_chunk=h/n
	print w_chunk
	print h_chunk
	t=n*m+1
	im_number=range(1,t)
	k=0
	img_ext=".jpg"
	for i in range(1,n+1):
		lt_h=h_chunk*(i-1)
		for j in range(1,m+1):
			lt_w=w_chunk*(j-1)
			split_name=str(im_number[k])
			split_name+=img_ext
			im.crop((lt_w,lt_h,lt_w+w_chunk,lt_h+h_chunk)).save(split_name)
			k=k+1
	merge_image(m,n,w,h)		

def image_read():
	im=Image.open("test.jpg")
	m=3
	n=3
	split_image(im,m,n)

def main():
	image_read()

if __name__ == "__main__":
	main()