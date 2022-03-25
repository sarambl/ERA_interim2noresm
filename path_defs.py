import calendar
from pathlib import Path

# Edit this path:
data_folder = Path('/Users/sarablichner/code_stuff/ERAinterim2noresm/Data')
# can be created from history file with adding option to download_and_compute.py or by running make_res_file.py
res_file = data_folder / 'resfile_f19_tn14_h0.nc'


# No need to edit:
dic_month = dict((k, v.lower()) for k, v in enumerate(calendar.month_abbr))
input_folder = data_folder / 'rawdata'
res_file_T = data_folder / f'{res_file.name[:-3]}_T.nc'
vct_file = data_folder / 'vct_fixed.txt'
tmp_folder = data_folder / 'tmp_data'
out_folder = data_folder / 'outdata'
