import glob, os
from random import shuffle

current_dir = "/home/ayush/Projects/object_detection_ws/src/research/dataset_creation/Images/"
txt_glob = glob.iglob(os.path.join(current_dir, "*.txt"))
jpg_glob = glob.iglob(os.path.join(current_dir, "*.jpg"))
txt_titles = []
jpg_titles = []

for pathAndFilename in txt_glob:
    title = os.path.splitext(pathAndFilename)[0]
    txt_titles.append(title)
    print("File title: {}.txt".format(title))

for pathAndFilename in jpg_glob:
    title = os.path.splitext(pathAndFilename)[0]
    jpg_titles.append(title)
    print("File title: {}.jpg".format(title))

for name in jpg_titles:
	print("here")
	if name not in txt_titles:
		os.remove(str(name)+".jpg") 
		print("removing")

