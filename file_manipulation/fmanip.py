''' 
    This file is a framework program in order to explore how to access and
    manipulate the data obtained through GPR A-scans 
    
    parts taken from gprMax/tools/plot_Ascan.py
'''

import h5py
import numpy as np

from gprMax.exceptions import CmdInputError
from gprMax.receivers import Rx
from gprMax.utilities import fft_power


f = h5py.File('heterogeneous_soil1.out', 'r')
nrx = f.attrs['nrx']
dt = f.attrs['dt']
iterations = f.attrs['Iterations']
time = np.linspace(0, (iterations - 1) * dt, num=iterations)


print(f.keys())

for val in f['rxs']['rx1'].values():
    print(val)

print(f['srcs'])

f.close()