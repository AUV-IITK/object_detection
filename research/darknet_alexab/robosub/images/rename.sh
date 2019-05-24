i=0
for f in ./Pictures/*.*
do 
	echo "Starting renaming the file : -$f"
	mv $f "$i".jpg
	echo "Renamed for the file number i = $i"
	i=$((i+1))
	echo "--------------------------------------------------"
done
