for i in ls -rRpm ; do
  mv /home/nick/TwitterSearchToDatabase/queries_for_amita/*$i* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism
done

for file in ./tiles_to_add/*.zip; do
  unzip -o $file -d ../tiles/file/
done

for file in ./tiles_to_add/*.zip;
echo file