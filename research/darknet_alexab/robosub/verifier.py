import glob
path="/home/ayush/Projects/object_detection_ws/src/research/darknet_alexab/robosub/images/*.txt"
files=glob.glob(path)

for f in files:
  f_read = open(f,"r+")
  lines = [line.rstrip('\n') for line in f_read] 
  f_read.close()
  try:
    for line in lines:
        if(line is not "\n"):
            #print(line)
            num, rest = line.split(" ", 1)
            if (int(num)>4):
              #print(num)
              print(f)
  except:
    print("No line:")
