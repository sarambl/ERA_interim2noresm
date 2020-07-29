#Import required modules
import sys
from netCDF4 import Dataset
from scitools import *

vct_in = 'vct_wrong.txt'

infile = open(vct_in, 'r')
lines = infile.readlines()
infoline = lines[0]

lev = []
new_hyam = []
hybm = []

for line in lines[1:]:
	words = line.split()
	numbers = [float(w) for w in words]
	lev.append(int(numbers[0]))
	new_hyam.append((numbers[1])*100000)
	hybm.append(numbers[2])
infile.close()

vct_out = 'vct_right.txt'
outfile = open(vct_out, 'w')

outfile.write(infoline)

for i in range(0,len(lev)):
        outfile.write('%4d %25.17f %25.17f \n' %(lev[i], new_hyam[i], hybm[i]))
outfile.close()


