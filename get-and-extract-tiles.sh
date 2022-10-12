for i in ls -rRpm ; do
  mv /home/nick/TwitterSearchToDatabase/queries_for_amita/*$i* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism
done

for file in ./tiles_to_add/*.zip; do
  unzip -o $file -d ../tiles/file/
done


# for extracting the tiles

for file in ./tiles_to_add/*.zip; do
filename=$(basename -- "$file")
filename="${filename%.*}"
outdir="../tiles/$filename"
mkdir -p $outdir
unzip -q -o $file -d $outdir
done

# for moving the tiles
for file in ./tiles_to_add/*.zip; do
mv $file ./existing_tiles/
git add . && git commit -m "Added $file tiles" && git push
done
