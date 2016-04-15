from PIL import Image
import glob
def main():
	Images=glob.glob('*.JPEG')
	maxw=0
	maxh=0
	j=0
	for I in Images:
		print j
		im=Image.open(I)
		w,h=im.size
		if maxw<w:
			maxw=w
		if maxh<h:
			maxh=h
		j=j+1
	print maxh
	print maxw
	print max(maxh,maxw)

if __name__ == "__main__":
	main()
