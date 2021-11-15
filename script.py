import pandas as pd
import numpy as np
import os
import sys

from module import *



path = '/Users/bahadirogluej/Desktop/Cisplatin GvHD/'

controls = [pd.read_csv(path+'standardized_csv/'+item) for item in os.listdir(path+'standardized_csv') if 'Dminus1' in item]
print('calculating coefficients')
coefs = batch_correction(controls[0], controls[1])
print('applying transformation')
apply_transformation(controls[1], coefs)