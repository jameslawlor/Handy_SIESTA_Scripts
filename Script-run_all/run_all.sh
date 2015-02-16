for i in $(ls -d */);
do
	echo ${i%%/}
	cd $i
	echo ${PWD}
	siesta < *.fdf | tee cnt.out
	cd ../
done
