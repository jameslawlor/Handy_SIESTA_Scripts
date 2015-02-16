import fileinput


for line in fileinput.input():
	mc = (line.split("_")[3]).split("/")[0]
	kval = line.split("_")[1]
	mc = (line.split("_")[3]).split("/")[0]
	E = (line.split(" ")[-1]).split("\n")[0]
	path1 = 'ETOT_vs_kval.dat_at_meshcut_'+str(mc)+'.dat'
	path2 = 'ETOT_vs_meshcut_at_kval_'+str(kval)+'.dat'
	f1 = open(path1,'a')
	f2 = open(path2,'a')
	f1.write( kval + "\t" + E + "\n")
	f2.write( mc + "\t" + E + "\n")

