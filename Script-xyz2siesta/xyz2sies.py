from os import listdir
from os.path import isfile, join, exists

# First we need to check we have the FDF template and some XSF files to work with

xyz_lst = []

for f in [ f for f in listdir(".") if isfile(join(".",f)) ]:
	if f.endswith(".xyz"): xyz_lst += [f] ; print 'XYZ file found!'

x_translation = float(raw_input('What is the desired x translation (ang)?'))
y_translation = float(raw_input('What is the desired y translation (ang)?'))
z_translation = float(raw_input('What is the desired z translation (ang)?'))

for f in xyz_lst:

	path = f.split('.')[0]	
	d = open(f,'r').readlines()
	f2 = open(path+'.xyz2sies','w')
	
	el_dic = {}
	
	# Gets number of atoms from top of file
	num_atoms = int(d[0].split()[0])
	del d[0:2]	# Deletes the number of atoms, leaving only the table of element type and coordinate
	
	counter = 1 	# Counter for how many unique atomic species we have, to be used for labelling in the output file.
	
	for line in d:
		l = line.split()
		if l and l[0] not in el_dic:
			el_dic[l[0]] = counter
			counter += 1
	
	for line in d:
		l = line.split()
		x_coord = str.format("{:8f}",(float(l[1]) + x_translation))
		y_coord = str.format("{:8f}",(float(l[2]) + y_translation))
		z_coord = str.format("{:8f}",(float(l[3]) + z_translation))
		element_type = str(el_dic[l[0]])
		f2.write("\t".join([x_coord,y_coord,z_coord,element_type,"\n"]))
	
	print 200*"-"
	print 200*"-"
	print 8*'\t' , "IMPORTANT! Don't forget to change the FDF file AtomicSpecies and Coordinates!!!" 
	print 10*'\t' , " New XYZ file located at" , path 
	print 200*"-"
	print 200*"-"


