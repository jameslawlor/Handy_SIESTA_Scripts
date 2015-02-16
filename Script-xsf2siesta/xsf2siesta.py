# We want this script to take in a XSF file and create an FDF from it, using a template

from os import listdir
from os.path import isfile, join, exists

xsf_lst = []

# First we need to check we have the FDF template and some XSF files to work with
for f in [ f for f in listdir(".") if isfile(join(".",f)) ]:
	if f.endswith("template.fdf"): fdf_template = f ; print 'FDF Template found!'
	if f.endswith(".xsf"): xsf_lst += [f] ; print 'XSF File found!'


for f in xsf_lst:	# Runs over the different cell sizes
	fdf_data = open(fdf_template,"r").readlines()	# we want to alter this data for each cell size, so probably better to recreate it each time we run the loop

	# We need to remove the current coordinates in the FDF data
	line_num = 0
	while line_num < len(fdf_data):
		if fdf_data[line_num] == "%block AtomicCoordinatesAndAtomicSpecies\n" :
			line_num += 1
			while fdf_data[line_num] != "%endblock AtomicCoordinatesAndAtomicSpecies\n":
				del fdf_data[line_num]
			line_num += 1
		else: line_num += 1



	size = f[0]
	out = open(f[0]+"x"+f[0]+'.fdf','w')	# Creates an output FDF file
	xsf_data = open(f,"r").readlines()		# Gets xsf data from the file we are currently looping onto
	num_atoms = 2*int(f[0])**2			# Number of atoms to expect

	line_num = 0
	coords = []
	while line_num < len(xsf_data)-1:		# Iterate through the XSF data. We first need to grab the coordinates of all the atoms from the XSF data
		if xsf_data[line_num] == ' ATOMS\n':
			for _ in range(num_atoms):
				line_num+= 1
				coords += [xsf_data[line_num].split()[1:]]
		else: line_num += 1

	# Now using the COORDS we saved, we can add them into the FDF data and then output to a file
	line_num = 0
	while line_num < len(fdf_data)-1 :
		if fdf_data[line_num] and fdf_data[line_num].split(" ")[0] == "NumberOfAtoms":		# Don't forget to change the number of atoms!
			fdf_data[line_num] = "NumberOfAtoms \t"+str(num_atoms) + "\n"
			line_num += 1

		if fdf_data[line_num] ==  "%block AtomicCoordinatesAndAtomicSpecies\n":			# Pastes in Coordinates 
			for site in coords:
				fdf_data.insert(line_num+1, site[0] + "\t" + site[1] + "\t" + site[2] + "\t 1"+"\n")	# Insert into output data
	
		if fdf_data[line_num] and fdf_data[line_num].split(" ")[0] == "LatticeConstant":	# Scales Lattice Constant according to size of unit cell
			fdf_data[line_num] = "LatticeConstant \t"+str(float(size) * float( (fdf_data[line_num].split(5*" ")[1]).split(" ")[0]  ) )+" Ang\n"
			line_num += 1
		line_num += 1

	for line in fdf_data:
		out.write(line)	

