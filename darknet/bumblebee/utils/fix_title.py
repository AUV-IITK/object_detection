 #!/usr/bin/python
import string, glob, os

current_dir = "/media/ayush/DATA1/Data/dices_yolo/labels_yolo"
print(current_dir)
labels_glob = glob.iglob(os.path.join(current_dir, "*.txt"))

for pathAndFilename in labels_glob:
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    changed_title = (title.split("_yolo")[0])
    print(changed_title)
    os.rename(title + ".txt", changed_title + ".txt")

print("Conversion done")