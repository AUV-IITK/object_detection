i=0
for f in *.MP4
do 
	echo "Starting conversion for the following video: -$f"
	ffmpeg -i $f -vf fps=1 ./"$i"%04d.jpg -hide_banner
	echo "Conversion done for the file number i = $i"
	i=$((i+1))
	echo "--------------------------------------------------"
done
