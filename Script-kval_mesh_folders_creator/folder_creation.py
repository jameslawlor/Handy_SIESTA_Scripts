from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil

""" This program will generate a batch of folders corresponding to a range of k-value and mesh cutoffs, labelling accordingly """
""" We require a template FDF file in the same directory as this program, which will be modified and copied to each folder, along with any required PSF files (must also be located in this dir)"""

psf_lst = []

# Searches current directory and gets name+location of psf and fdf files
for f in [ f for f in listdir(".") if isfile(join(".",f)) ]:
	if f.endswith(".psf"): psf_lst += [f] ; print 'PSF found!'
	if f.endswith(".fdf"): fdf_template = f ; print 'FDF found!'

# Desired kpts and MeshCutoffs
klist = range(4,11,2)
meshlist = range(200,401,50)

# Checks for errors in the FDF file
checker = [False, False]

for k in klist:
	for m in meshlist:
		newpath = 'kval_'+str(k)+'_meshval_'+str(m)	# Creates new directory for given kpt and cutoff
		if not exists(newpath): makedirs(newpath)		

		for psf in psf_lst: shutil.copy2(psf, newpath+"/"+psf)	#Copies all Pseudopotential files to the new directory


		# Now we will copy over the FDF file line by line, but making the changes to the KPTS and cutoff lines
		fdf_data = open(fdf_template,"r").readlines()
		line_num = 0
		while line_num < len(fdf_data)-1:		
			if fdf_data[line_num] ==  '%block kgrid_Monkhorst_Pack\n':					# Changes the KPTs data
				fdf_data[line_num + 1]  = " " + "\t".join([str(k),"0","0","0.0"]) + '\n'
				fdf_data[line_num + 2]  = " " + "\t".join(["0",str(k),"0","0.0"]) + '\n'
				fdf_data[line_num + 3]  = " " + "\t".join(["0","0","1","0.0"]) + '\n'
				line_num += 5
				checker[0] = True

			elif fdf_data[line_num].split() and fdf_data[line_num].split()[0] == 'MeshCutoff':		# Changes cutoff data
				checker[1] = True
				fdf_data[line_num] = 'MeshCutoff' + '\t' + str(float(m)) + ' Ry \n'
				line_num += 1
			else:
				line_num += 1
		
		
		if sum(checker) != 2:									# Checks both cutoff and KPTS have been changed
			print ' ERRORS! Check kgrid and MeshCutoff!'
		else:											# Creates the new FDF file in chosen kpt/cutoff path
			new_fdf_file = open(newpath+'/graphene.fdf','w')
			for line in fdf_data:
				new_fdf_file.write(str(line))
			new_fdf_file.close()

