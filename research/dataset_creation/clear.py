import glob, os
from random import shuffle

current_dir = "/home/ayush/Projects/object_detection_ws/src/research/darknet_alexab/vampire/Images"
txt_glob = glob.iglob(os.path.join(current_dir, "*.txt"))
txt_titles = []

for pathAndFilename in txt_glob:
	print(pathAndFilename)
	f = open(pathAndFilename, "r")
	contents = f.read()
	contents_string = str(contents)
	contents_string = contents_string.split(" ", 1)[1]
	contents_string = "0 " + contents_string
	print(contents_string)
	f.close()
	f = open(pathAndFilename, "w+")
	f.write(contents_string)

