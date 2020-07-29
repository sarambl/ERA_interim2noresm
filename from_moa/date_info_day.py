"""
Making date and datesec arrays in netcdf format that we can
add to the ERA-interim metdata file so it can be used to nudge NorESM

Required modifications before you run it:
Insert information about the starting date, the length of the year and the length of february
Remember also to change the time.units so it matches the first date of your file. 

Run it like this: python date_info_day.py 2001-01-01
"""

#Import required modules
import sys
from netCDF4 import Dataset
from scitools import *
from numpy import dtype


# Read in netCDF-files
date = str(sys.argv[1])
infile = './' + date + '.nc'

# prepare date
year,mon,day = date.split('-')
year_num = int(float(year))
mon_num = int(float(mon))
day_num = int(float(day))


datesec_calc = []
val_pr_day = 4
secstep = 86400/val_pr_day
sec = [0, 1*secstep, 2*secstep, 3*secstep]
for j in sec:
        datesec_calc.append(j)

# Open a netCDF file for appending:
ncfile = Dataset(infile,'a')
time_in = ncfile.variables['time'][:]
#ncfile = Dataset('date_datesec' + date + '.nc','w') 

# Create the variable (4 byte integer in this case)
# first argument is name of variable, second is datatype, third is
# a tuple with the names of dimensions.
date = ncfile.createVariable('date',dtype('int32').char,('time'))
datesec = ncfile.createVariable('datesec',dtype('int32').char,('time'))

# Write data to variable:
date[:] = year_num*10000+mon_num*100+day_num
datesec[:] = datesec_calc

# Add attributes to the variables:
date.long_name = 'current date (YYYYMMDD)'
datesec.long_name = 'current seconds of current date'

# close the file.
ncfile.close()
