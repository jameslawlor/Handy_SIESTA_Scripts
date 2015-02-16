#doped_system_path = raw_input("What is the name of the DOPED system? ") + ".out"
#pristine_system_path = raw_input("And the name of the PRISTINE system? ") + ".out"
doped_system_path = 'system_A_relaxation.out'
pristine_system_path = 'system_B_relaxation.out'

host_atoms = 98

fdope_orig = open(doped_system_path).readlines()
fpris_orig = open(pristine_system_path).readlines()

fdope , fpris = [], []
# Remove blank lines
for f , g in [[fdope_orig,fdope],[fpris_orig, fpris]]:
	for line in f:
		if line.strip():
			g += [line.split()]

# First sum up the charge on the pristine system
line_num = 0
while line_num < (len(fpris)):
	if fpris[line_num][0] == 'mulliken:' and fpris[line_num][1] == 'Mulliken': # Finds Mulliken Population Info
		while fpris[line_num][0] != '1': line_num += 1	# Skips to first atom line
		atom_num = 1
		Qtot = float(fpris[line_num][1])
		while atom_num < host_atoms:	# Iterate through list of host atoms
			if fpris[line_num][0] == str(atom_num + 1):	# If line has info on next atom
				Qtot += float(fpris[line_num][1])
				atom_num += 1
				line_num += 1
			
			line_num += 1

		
	line_num+=1

# Save charge result and reintialise
Qtot_pris = Qtot
Qtot = 0
line_num = 0

while line_num < (len(fdope)):
        if fdope[line_num][0] == 'mulliken:' and fdope[line_num][1] == 'Mulliken': # Finds Mulliken Population Info
                while fdope[line_num][0] != '1': line_num += 1  # Skips to first atom line
                atom_num = 1
                Qtot = float(fdope[line_num][1])
                while atom_num < host_atoms:    # Iterate through list of host atoms
                        if fdope[line_num][0] == str(atom_num + 1):     # If line has info on next atom
                                Qtot += float(fdope[line_num][1])
                                atom_num += 1
                                line_num += 1

                        line_num += 1


        line_num+=1

Qtot_doped = Qtot

print 'Difference in Charge Populations between the host in the Doped and Pristine Systems is ' , str(Qtot_doped - Qtot_pris)
