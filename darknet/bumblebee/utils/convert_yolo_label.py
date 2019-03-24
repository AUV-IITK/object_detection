 #!/usr/bin/python
image_width = 1024
image_height = 768
import string, glob, os

current_dir = "/media/ayush/DATA1/Data/ml_bumblebee/labels"
print(current_dir)
labels_glob = glob.iglob(os.path.join(current_dir, "*.txt"))

for pathAndFilename in labels_glob:
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    s = open(title + ".txt","r+")
    f = open(title + "_yolo.txt", "w+")
    count = 0
    for line in s.readlines():
        
        if count != 0:
        
            str_x_min, str_y_min, str_x_max, str_y_max, str_dice_id = line.split()
            x_min = int(str_x_min)
            y_min = int(str_y_min)
            x_max = int(str_x_max)
            y_max = int(str_y_max)
            if str_dice_id == 'dice1':
                dice_id = 0
            elif str_dice_id == 'dice2':
                dice_id = 1
            elif str_dice_id == 'dice5':
                dice_id = 2
            elif str_dice_id == 'dice6':
                dice_id = 3
            else:
                dice_id = 4      
            print (x_min, x_max, y_min, y_max, dice_id)
            x_center = (x_min+x_max)/2
            y_center = (y_min+y_max)/2
            width = x_max - x_min
            height = y_max - y_min
            x_center_normalised = round(((float)(x_center))/image_width, 6)
            y_center_normalised = round(((float)(y_center))/image_height, 6)
            width_normalised = round(((float)(width))/image_width, 6)
            height_normalised = round(((float)(height))/image_height, 6)
            print(dice_id, x_center_normalised, y_center_normalised, width_normalised, height_normalised)
            f.write("{} {} {} {} {}\n".format(dice_id, x_center_normalised, y_center_normalised, width_normalised, height_normalised))
        
        count+=1
    s.close()
    f.close()

print("Conversion done")