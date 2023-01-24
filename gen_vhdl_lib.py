from operator import mod
import os
import toml

dir_path = "ip/common/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
mod_dict = {}
file_list = {}
name_list = {}

for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

dir_path = "ip/ecc/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

mod_dict['libraries'] = name_list

dir_path = "ip/dsp/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

mod_dict['libraries'] = name_list

dir_path = "ip/swift_bsp/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

mod_dict['libraries'] = name_list

dir_path = "ip/xilinx/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

mod_dict['libraries'] = name_list

dir_path = "ip/vivado/MyProcessorIPLib/pcores"
dir_list = os.listdir(dir_path)
for name in dir_list:
    if os.path.isdir(f'{dir_path}/{name}/hdl/vhdl'):
        file_list = {}
        file_list['files'] = [f'{dir_path}/{name}/hdl/vhdl/*.vhd']
        name_list[name] = file_list

mod_dict['libraries'] = name_list

f = open('vhdl_ls.toml','w')
toml.dump(mod_dict,f)
f.close()