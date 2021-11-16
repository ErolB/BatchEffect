import sys
import getopt
from module import *
import pickle as pkl
import pandas as pd
from numpy import log1p

apply_log = True

if __name__ == '__main__':
    argv = sys.argv
    opts, args = getopt.getopt(sys.argv[1:], 'i:o:c:', ['disable_log', 'name='])
    arg_dict = {item[0]: item[1] for item in opts}
    if '--disable_log' in arg_dict.keys():
        apply_log = False
    input_file = arg_dict['-i']
    input_frame = pd.read_csv(input_file)
    if apply_log:
        input_frame = log1p(input_frame)
    output_file = arg_dict['-o']
    coef_file = arg_dict['-c']
    with open(coef_file, 'rb') as coef_file_obj:
        coefs = pkl.load(coef_file_obj)
    corrected_data = apply_transformation(input_frame, coefs)
    corrected_data.to_csv(output_file)
