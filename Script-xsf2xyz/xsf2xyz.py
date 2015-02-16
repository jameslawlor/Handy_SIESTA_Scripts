from os import listdir
from os.path import isfile, join, exists

xsf_lst = []

# First we need to check we have the FDF template and some XSF files to work with
for f in [ f for f in listdir(".") if isfile(join(".",f)) ]:
        if f.endswith(".xsf"): xsf_lst += [f] ; print 'XSF File found!'

for path in xsf_lst:
        xsf_data = open(path,"r").readlines()              # Gets xsf data from the file we are currently looping onto

	outf = open(path.split(".")[0]+'.xyz','w')	   # Makes XYZ output file with corresponding name to input

	num_atoms = 2*int(path[0])**2
	outf.write('\t' + str(num_atoms) + '\n' + '\n') # Writes header of XYZ file stating number of atoms

        coords = []
        line_num = 0
	atom_label_list = []
        while line_num < len(xsf_data)-1:               # Iterate through the XSF data. We first need to grab the coordinates of all the atoms from the XSF data
                if xsf_data[line_num] == ' ATOMS\n':
                        for _ in range(num_atoms):
                                line_num+= 1
                                coords += [xsf_data[line_num].split()[:]]
				atom_label_list += [xsf_data[line_num].split()[0]] # Atom label
                else: line_num += 1

	atom_labels_dict = {}	# Makes dictionary of atom labels, the key is atomic number and entry is chemical symbol
	for atom in set(atom_label_list):	# Iterate through unique atoms in our input
		atom_labels_dict[atom] = raw_input("What is the chemical symbol for the atom denoted " + str(atom) + '?')

	for site in coords:	# Time to generate the output XYZ
		label = atom_labels_dict[site[0]]
		x_coord = str.format("{:5f}",(float(site[1])))
		y_coord = str.format("{:5f}",(float(site[2])))
		z_coord = str.format("{:5f}",(float(site[3])))
		outf.write("\t".join([label,x_coord,y_coord,z_coord,"\n"]))
#		print site		

