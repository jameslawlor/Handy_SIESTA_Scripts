import os
import numpy as np
from os.path import isfile, join, exists

lattice_constant = float(raw_input("Please give the lattice constant from the original FDF file in Angstroms: "))

bohr_radius =  0.5292

for f in [ f for f in os.listdir(".") if isfile(join(".",f)) ]:
	if f.endswith(".XV"): xv_file = f ; print 'XV file found!'

with open(xv_file) as f:
	d = f.readlines()[:3]
	vecs = []
	for line in d:
		 vecs += [[float(x) for x in line.split()][:3]]		# Gets the 3 unit vectors

	vecs = np.array(vecs) * bohr_radius / lattice_constant	# Converts unit vectors to Angstrom
						# FDF files require a lattice constant and the unit vectors to be given in units of this constant, hence
						# if we require this program to provide input to the FDF file we gotta do this
	fout = open(xv_file.split(".")[0]+'_FDF_READABLE_OUTPUT.txt',"w")
	fout.write('Lattice Constant Used = ' + str(lattice_constant) + "\n" + "\n")
	fout.write('Lattice Vectors are:' + "\n")
	for l in vecs:
		fout.write( "\t".join(str(x) for x in l) + "\n")
	fout.close()
