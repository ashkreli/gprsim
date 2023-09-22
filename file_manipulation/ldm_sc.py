## Center of mine placed exactly 15 cm below the ground

f = open('ldm_sc.in', 'w')

dx = 0.002
dy = dx
dz = dy

f.write(f"""
#title: PMA landmine in heterogeneous soil        

#dx_dy_dz: {dx} {dy} {dz}
#time_window: 6e-9

#waveform: ricker 1 1.4e9 my_ricker

#soil_peplinski: 0.5 0.5 2.0 2.66 0.005 0.25 my_soil
    """)


## World dimensions (in meters)
## z is the upright height in our frame
wd_dim = (0.5, 0.5, 0.4)

## Dimensions of fractal box of soil
fb_dim = (wd_dim[0], wd_dim[1], 0.25)

## Dimensions of PMA mine - from README in landmine_models folder
ldm_dim = (0.14, 0.064, 0.034)

## Placement of receiver array
arr_pos = (fb_dim[0]/2 - ldm_dim[0]/2 - 0.05, fb_dim[1]/2, fb_dim[2] + 0.05)
spc = 0.06

f.write(f"""
#domain: {wd_dim[0]} {wd_dim[1]} {wd_dim[2]}

#fractal_box: 0 0 0 {fb_dim[0]} {fb_dim[1]} {fb_dim[2]} 1.5 1 1 1 8 my_soil my_soil_box
#geometry_objects_read: {fb_dim[0]/2 - ldm_dim[0]/2} {fb_dim[1]/2 - ldm_dim[1]/2} {0.15 - ldm_dim[2]/2} ../gprMax/user_libs/landmine_models/PMA_2x2x2.h5 ../gprMax/user_libs/landmine_models/PMA_materials.txt

#rx: {arr_pos[0] - spc} {arr_pos[1] - spc} {arr_pos[2]}
#rx: {arr_pos[0]} {arr_pos[1] - spc} {arr_pos[2]}
#rx: {arr_pos[0] + spc} {arr_pos[1] - spc} {arr_pos[2]}

#rx: {arr_pos[0] - spc} {arr_pos[1]} {arr_pos[2]}
#hertzian_dipole: y {arr_pos[0]} {arr_pos[1]} {arr_pos[2]} my_ricker
#rx: {arr_pos[0] + spc} {arr_pos[1]} {arr_pos[2]}

#rx: {arr_pos[0] - spc} {arr_pos[1] + spc} {arr_pos[2]}
#rx: {arr_pos[0]} {arr_pos[1] + spc} {arr_pos[2]}
#rx: {arr_pos[0] + spc} {arr_pos[1] + spc} {arr_pos[2]}

#src_steps: 0.002 0 0
#rx_steps: 0.002 0 0

#geometry_view: 0 0 0 {wd_dim[0]} {wd_dim[1]} {wd_dim[2]} 0.002 0.002 0.002 ldm_sc n
#snapshot: {arr_pos[0] - spc} {arr_pos[1] - spc} {arr_pos[2] - spc} {arr_pos[0] + spc} {arr_pos[1] + spc} {arr_pos[2] + spc} 0.002 0.002 0.002 2e-9 ldm_sc
    """)


f.close()