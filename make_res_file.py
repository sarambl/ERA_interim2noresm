from subprocess import run
import sys
from path_defs import res_file


# %%

def main(h0_file, outfolder=None):
    """

    :param h0_file: monthly history file to be used to create correct grid.
    :param outfolder: where to put the  output file
    :return:
    """
    # %%

    if outfolder is None:
        path_outfile = res_file
    else:
        path_outfile = outfolder + '/resfile_f19_tn14_h0.nc'
    cdo_com = f'ncks -v T,hyai,hybi,hyam,hybm {h0_file} {str(path_outfile)}'
    run(cdo_com, shell=True)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Lacking input file \n Correct usage: '
                 'python conv_ERA_interim.py <h0_history_file>')

    h0_file = sys.argv[1]
    if len(sys.argv) > 2:
        outfolder = sys.argv[2]
        main(h0_file, outfolder=outfolder)
    else:
        main(h0_file)

# cdo -s selname,T ../ERA_f19_tn14/res_file_T.nc ./res_file_T.nc\n
# %%
