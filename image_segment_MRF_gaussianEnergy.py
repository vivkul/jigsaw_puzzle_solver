from PIL import Image
import numpy as np 
from itertools import permutations
import glob
from scipy.stats import norm

Map=np.empty([2, 4, 4])
per_index=list(enumerate(''.join(p) for p in permutations('1234')))
max_dimention=2184
gaussian_array=np.empty([max_dimention])

def get_energy_quad(i,j,orientation,im):
	image_width,image_height=im.size
	m=n=2
	w_chunk1=image_width/m
	w_chunk2=image_width-w_chunk1
	h_chunk1=image_height/n
	h_chunk2=image_height-h_chunk1
	im_matrix=np.asarray(im)
	if orientation==0:
		x_top=(i/m)*h_chunk1
		if i/m==0:
			x_bot=h_chunk1-1
		else:
			x_bot=image_height-1
		if i%m==0:
			x_right=w_chunk1-1
		else:
			x_right=image_width-1
		y_top=(j/m)*h_chunk1
		if j/m==0:
			y_bot=h_chunk1-1
		else:
			y_bot=image_height-1
		y_left=(j%m)*w_chunk1
		sum_=0
		h_chunk=min(h_chunk1,h_chunk2)
		w_chunk=min(w_chunk1,w_chunk2)
		if im_matrix[0,0].size == 1:
			for l in range(h_chunk):
				addr=0
				for b in range(min(w_chunk,20)):
					addr=addr+gaussian_array[b]*np.square(im_matrix[x_top+l,x_right-b]-im_matrix[y_top+l,y_left+b])
				sum_=sum_+addr/(min(w_chunk,20)*1.0)
		else:
			for l in range(h_chunk):
				addr=0
				for b in range(min(w_chunk,20)):
					addr=addr+gaussian_array[b]*sum(np.square(im_matrix[x_top+l,x_right-b]-im_matrix[y_top+l,y_left+b]))
				sum_=sum_+addr/(min(w_chunk,20)*1.0)
		return sum_/(h_chunk*1.0)
	else:
		if i/m==0:
			x_bot=h_chunk1-1
		else:
			x_bot=image_height-1
		x_left=(i%m)*w_chunk1
		if i%m==0:
			x_right=w_chunk1-1
		else:
			x_right=image_width-1
		y_top=(j/m)*h_chunk1
		y_left=(j%m)*w_chunk1
		if j%m==0:
			y_right=w_chunk1-1
		else:
			y_right=image_width-1
		sum_=0
		w_chunk=min(w_chunk1,w_chunk2)
		h_chunk=min(h_chunk1,h_chunk2)
		if im_matrix[0,0].size == 1:
			for l in range(w_chunk):
				addr=0
				for b in range(min(h_chunk,20)):
					addr=addr+gaussian_array[b]*np.square(im_matrix[x_bot-b,x_left+l]-im_matrix[y_top+b,y_left+l])
				sum_=sum_+addr/(min(h_chunk,20)*1.0)
		else:
			for l in range(w_chunk):
				addr=0
				for b in range(min(h_chunk,20)):
					addr=addr+gaussian_array[b]*sum(np.square(im_matrix[x_bot-b,x_left+l]-im_matrix[y_top+b,y_left+l]))
				sum_=sum_+addr/(min(h_chunk,20)*1.0)
		return sum_/(w_chunk*1.0)

def pre_compute_energy(im):
	global Map
	w,h=im.size
	l=max(w/2,h/2)
	
	for i in range(4):
		for j in range(i+1,4):
			Map[0,i,j]=get_energy_quad(i,j,0,im)		#When i is on left of j
			Map[0,j,i]=get_energy_quad(j,i,0,im)		#When j is on left of i
			Map[1,i,j]=get_energy_quad(i,j,1,im)		#When i is on top of j
			Map[1,j,i]=get_energy_quad(j,i,1,im)		#When j is on top of i

def find_optimal_permutation():
	Energy_array = np.empty([24])
	for in_idx, in_ in per_index:
		a = int(in_[0])-1
		b = int(in_[1])-1
		c = int(in_[2])-1
		d = int(in_[3])-1
		Energy_array[in_idx] = Map[0,a,b]+Map[0,c,d]+Map[1,a,c]+Map[1,b,d]
	return np.argmin(Energy_array)

def image_read(I):
	im=Image.open(I)
	w,h=im.size
	m=2
	n=2
	# if w%m==0 and h%n==0:
	pre_compute_energy(im)
	del im
	return find_optimal_permutation()

	# else:
	# 	print "size not multiple of 2 for"
	# 	print I
	# 	del im
	# 	return -1

def main():
	global gaussian_array
	for i in range(max_dimention):
		gaussian_array[i]=norm.pdf(i)
	Images=glob.glob('*.JPEG')
	j=0
	correct=0
	for I in Images:
		res=image_read(I)
		if res==-1:
			j-=1
		elif res==0:
			correct=correct+1
		j+=1
		print j
		print correct
	print correct/(j*1.0)

if __name__ == "__main__":
	main()
