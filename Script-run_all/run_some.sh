for i in $(ls -d */);
do
	if [ $i != "perturbed_full/" ]
	then
	        echo ${i%%/}
        	cd $i
		mpirun siesta < 6AGNR_H_L7.fdf > 6AGNR_H_L7.out
	        cd ../
	fi
done

