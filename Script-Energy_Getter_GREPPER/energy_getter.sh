#!/bin/bash

grep -nr --exclude=energy_getter.sh  'siesta:         Total =' . > temp.dat	# Grabs total energy values from different KVAL and Mesh files
rm -r ETOT*.dat
python energy_getter.py < temp.dat
rm temp.dat



