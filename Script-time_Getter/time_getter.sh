#!/bin/bash

grep -nr --exclude=time_getter.sh  'elaps:  siesta        ' .   > _temp.dat	# Grabs time taken for calc from each kval/mc file
rm -r time*.dat
python time_getter.py < _temp.dat
rm _temp.dat



