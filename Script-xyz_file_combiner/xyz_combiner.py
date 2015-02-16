# For combining XYZ files made through VMD into a single XYZ file

# Input: 1) 'Base' layer / host
# Input: 2) Range of input files with the specified impurity chemical formula prefix (i.e. "OH_*.xyz")

# Output: 3) Combines host + impurity XYZ files and spits out a single XYZ file containing 

from os import listdir
from os.path import isfile, join, exists

base_cell = raw_input('What is the name of the base cell input file? ')
impurity_prefix = raw_input('What is the impurity? ')

#base_cell = '7x7.xyz'
#impurity_prefix = 'OH'

xyz_list = []

# First we need to check for the XYZ files, ignoring the base input cell (i.e. the graphene layer) and the original XYZ input file for the molecule location 
# before it was moved with VMD
for f in [ f for f in listdir(".") if isfile(join(".",f)) ]:
        if f.startswith(impurity_prefix) and  f.endswith(".xyz") and not f == base_cell and not 'initial' in f : xyz_list += [f] ; print f

for f in xyz_list:
	outf = open( base_cell.split(".")[0] + '_' + f ,'w')	# Makes the output file for the combined XYZ files

	inf = open(f, 'r')
	base = open(base_cell,'r')	# opens up base cell for reading coords

	total_number_of_atoms = int( open(base_cell,'r').readlines()[0].split()[0] ) + int( open(f,'r').readlines()[0].split()[0] )  # Add up total number of atoms from input files

	outf.write("\t".join([str(total_number_of_atoms), '\n', '\n' ]))

	for line in inf.readlines()[2:] + base.readlines()[2:]: # Now shove all combined data into the output file
		outf.write("\t".join([line.split()[0], line.split()[1], line.split()[2], line.split()[3], '\n']))
