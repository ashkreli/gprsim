# Getting the hang of maipulating HDF5 files using Python `h5py` package
# Either need to install h5py or activate the gprMax environment which uses it 
# https://stackoverflow.com/questions/28170623/how-to-read-hdf5-files-in-python

import h5py
import numpy as np
import matplotlib.pyplot as plt
import sys


# Read argument filename
f = h5py.File(sys.argv[1], 'r')
# Open a new file that will hold the merged data
nf = h5py.File(sys.argv[1][:len(sys.argv[1])-4] + '_comb.out', 'w')

# Act as though the merged data is data for the first receiver
nf_rxs = nf.create_group('rxs')
nf_rxs_rx1 = nf_rxs.create_group('rx1')

print("For troubleshooting: these are the top-level groups")
for key in f.keys():
    print(str(key) + ' of type ' + str(type(f[key])))

print(f['rxs'])
print(f['rxs'].keys())
#print(np.array(f['rxs']['rx1']['Ez'][0]))

# Naive adding - did not work even when removing rx4/5
adder = np.zeros(np.shape(f['rxs']['rx1']['Ez']))
for i in range(1, len(f['rxs']) + 1):
    #if i == 4 or i == 5:
    #   continue
    for j in range(len(f['rxs'][f'rx{i}']['Ez'])):
        # adding absolute values to avoid sign canceling
        #adder[j] = adder[j] + np.abs(np.array(f['rxs'][f'rx{i}']['Ez'][j]))
        adder[j] = adder[j] + np.array(f['rxs'][f'rx{i}']['Ez'][j])

# Truncate first 500 iterations
adder[:500] = 0


avg = 0
for k in range(len(adder)):
    avg = 0
    avg += adder[k]
avg /= len(adder)
nf_rxs_rx1['Ez'] = adder #- avg
#nf_rxs_rx1['Ez'] = adder
#print(adder[0])
# Will throw a numpy 'product' deprecation warning
# --- internal to the h5py implementation
nf.attrs.create('Title', f.attrs['Title'])
nf.attrs.create('nrx', len(nf['rxs'].keys()))
nf.attrs.create('dt', f.attrs['dt'])

# print(f.attrs['Iterations'])
# print(nf.attrs['dt'])

nf.close()
f.close()