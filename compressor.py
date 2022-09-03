import os
import sys
from PIL import Image

# define a function for
# compressing an image
def compressMe(file, verbose = False):
	
	# Get the path of the file
	filepath = os.path.join(os.getcwd(),
							file)
	
	# open the image
	picture = Image.open(filepath)
	
	picture.save("Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 10)
	return

def main():
	
	verbose = False
	
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	cwd = os.getcwd()

	formats = ('.jpg', '.jpeg')

	for file in os.listdir(cwd):
		
		# If the file format is JPG or JPEG
		if os.path.splitext(file)[1].lower() in formats:
			print('compressing', file)
			compressMe(file, verbose)

	print("Done")

# Driver code
if __name__ == "__main__":
	main()
