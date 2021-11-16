import sys
import getopt
from module import *
import pickle as pkl
import pandas as pd
from numpy import log1p

apply_log = True

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'r:o:', ['disable_log', 'name='])
    arg_dict = {item[0]: item[1] for item in opts}
    if '--disable_log' in arg_dict.keys():
        apply_log = False
    ref_file = arg_dict['-r']
    ref_frame = pd.read_csv(ref_file)
    other_file = arg_dict['-o']
    other_frame = pd.read_csv(other_file)
    if apply_log:
        ref_frame = log1p(ref_frame)
        other_frame = log1p(other_frame)
    coefs = batch_correction(ref_frame, other_frame)
    if '--name' not in arg_dict.keys():
        arg_dict['--name'] = 'default'
    with open('%s_coefs.pkl' % arg_dict['--name'], 'wb') as coef_file:
        pkl.dump(coefs, coef_file)

