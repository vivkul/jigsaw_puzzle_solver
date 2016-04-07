from PIL import Image
import numpy as np 
from itertools import permutations
import glob

Map=np.empty([2, 4, 4])
per_index=list(enumerate(''.join(p) for p in permutations('1234')))

def get_energy_quad(i,j,orientation,im):
	image_width,image_height=im.size
	m=n=2
	w_chunk=image_width/m
	h_chunk=image_height/n
	im_matrix=np.asarray(im)
	if orientation==0:
		x_top=(i/m)*h_chunk
		x_bot=(i/m+1)*h_chunk-1
		x_right=(i%m+1)*w_chunk-1
		y_top=(j/m)*h_chunk
		y_bot=(j/m+1)*h_chunk-1
		y_left=(j%m)*w_chunk
		sum_=0
		for l in range(h_chunk):
			sum_=sum_+sum(np.square(im_matrix[x_top+l,x_right]-im_matrix[y_top+l,y_left]))
		return sum_/(h_chunk*1.0)
	else:
		x_bot=(i/m+1)*h_chunk-1
		x_left=(i%m)*w_chunk
		x_right=(i%m+1)*w_chunk-1
		y_top=(j/m)*h_chunk
		y_left=(j%m)*w_chunk
		y_right=(j%m+1)*w_chunk-1
		sum_=0
		for l in range(w_chunk):
			sum_=sum_+sum(np.square(im_matrix[x_bot,x_left+l]-im_matrix[y_top,y_left+l]))
		return sum_/(w_chunk*1.0)

def pre_compute_energy(im):
	global Map
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
	if w%m==0 and h%n==0:
			pre_compute_energy(im)
			del im
			return find_optimal_permutation()

	else:
		print "size not multiple of 2 for"
		print I
		del im
		return -1

def main():
	Images=glob.glob('*.JPEG')
	j=0
	correct=0
	for I in Images:
		print j
		res=image_read(I)
		if res==-1:
			j-=1
		elif res==0:
			correct=correct+1
		j+=1
	print correct/(j*1.0)

if __name__ == "__main__":
	main()
