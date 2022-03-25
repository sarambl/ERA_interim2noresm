import sys

import conv_ERA_interim
import download_ERA_grb_files
import make_res_file

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Correct usage: python download_and_compute.py <star_year> <end_year> '
              '<optional:h0_history_file_for_grid>')
        sys.exit()
    syear = int(sys.argv[1])
    eyear = int(sys.argv[2])
    if len(sys.argv) > 3:
        make_res_file.main(sys.argv[3])

    # Download stuff
    for field_type in ['3D', 'surf']:
        download_ERA_grb_files.import_years(syear,
                                            eyear,
                                            fieldtype=field_type)
    # Convert to NorESM format
    for year in range(syear, eyear + 1):
        conv_ERA_interim.main(year)
