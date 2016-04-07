from PIL import Image
import numpy as np
import sys
import glob

def merge_image(m,n,image_width, image_height,I):
	name=I[:-5]
	t=n*m
	perm_list=set()
	while len(perm_list)<6:
		temp=range(t)
		np.random.shuffle(temp)
		perm_list.add(tuple(temp))
	w_chunk=image_width/m
	h_chunk=image_height/n
	img_ext=".JPEG"
	while len(perm_list)>0:
		k=0
		final_image=Image.new('RGB',(image_width,image_height))
		merge_order=perm_list.pop()
		order_txt=open(name+"_"+str(len(perm_list))+'.txt','a')
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
				del part_im
				k=k+1
		final_image.save(name+"_"+str(len(perm_list))+".JPEG")
		order_txt.close()

def split_image(im,m,n,I):
	w,h=im.size
	w_chunk=w/m
	h_chunk=h/n
	print I
	t=n*m+1
	im_number=range(1,t)
	k=0
	img_ext=".JPEG"
	for i in range(1,n+1):
		lt_h=h_chunk*(i-1)
		for j in range(1,m+1):
			lt_w=w_chunk*(j-1)
			split_name=str(im_number[k])
			split_name+=img_ext
			im.crop((lt_w,lt_h,lt_w+w_chunk,lt_h+h_chunk)).save(split_name)
			k=k+1
	merge_image(m,n,w,h,I)		

def image_read(I):
	im=Image.open(I)
	w,h=im.size
	m=2
	n=2
	if w%m==0 and h%n==0:
		try:
			split_image(im,m,n,I)
		except:
			print "error in image"
			print I
			print "error handled"
	else:
		print "size not multiple of 2 for"
		print I
	del im

def main():
	Images=glob.glob('*.JPEG')
	j=1
	for I in Images:
		print j
		image_read(I)
		j+=1

if __name__ == "__main__":
	main()
