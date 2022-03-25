# Install and prepare: 
Please see
http://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets
for instructions on adding credentials for downloading.
**IMPORTANT:** need to copy your credential file to $HOME/.ecmwfapirc

```shell
conda env create -f env.yml
conda activate ecmwf
```




# To make noresm input for nudging to ERA-Interim
- edit paths in [path_defs.py](path_defs.py), i.e. define where to download data etc. 
- run [download_and_compute.py](download_and_compute.py) as
```shell script
python download_and_compute.py <start_year> <end_year> <history_file_in_correct_grid>

```
### OR
Run: 
```shell
python make_res_file.py <history_file_in_correct_grid>
# Download data
python upload_era_interim_multiple.py <start_year> <end_year>
# convert each year: 
conv_ERA_interim.py <start_year>
conv_ERA_interim.py <next_year>
...
conv_ERA_interim.py <end_year>
```
Scripts found here:
- [make_res_file.py](make_res_file.py)
- [upload_era_interim_multiple.py](upload_era_interim_multiple.py)
- [conv_ERA_interim.py](conv_ERA_interim.py)