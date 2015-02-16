import fileinput


for line in fileinput.input():
	mc = (line.split("_")[3]).split("/")[0]
	kval = line.split("_")[1]
	time = (line.split()[-2])
	path1 = 'time_vs_kval_at_meshcut_'+str(mc)+'.dat'
	path2 = 'time_vs_meshcut_at_kval_'+str(kval)+'.dat'
	print path1, path2
	f1 = open(path1,'a')
	f2 = open(path2,'a')
	f1.write( kval + "\t" + time + "\n")
	f2.write( mc + "\t" + time + "\n")

