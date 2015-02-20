#!/bin/bash

#for i in L*; do mv "$i" "$i"_KelvinIO_BSSE ; done
for i in $(ls -d L*/)
	do
	cd $i
	echo $i
	python bsse_calculation.py
	cd ../
	done

