import glob
path="/home/sumant/sumant/*.txt"
files=glob.glob(path)

for f in files:
  f_read = open(f,"r+")
  lines = [line.rstrip('\n') for line in f_read] 
  f_read.close()
  data_new = ""
  print(lines)
  try:
    for line in lines:
        print("LINE" + line)
        if(line is not "\n"):
            num, rest = line.split(" ", 1)
            if num=='15':
                    new_num='0'
            elif num=='16':
                    new_num='2'
            elif num=='17':
                    new_num='1'
            print(new_num)
            print()
            new_line = new_num + " " + rest + "\n"
            data_new = data_new + new_line
            print("DATA_NEW" + data_new)
    f_write = open(f, "w")
    f_write.write(data_new)
    f_write.close()
  except:
    print("No line:")
