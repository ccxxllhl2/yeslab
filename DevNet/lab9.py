'''
YAML 实验
'''


import yaml



with open('data/amcl_params.yaml') as f:
    data_str = f.read()
    data_yaml = yaml.load(data_str, Loader=yaml.FullLoader)

print(data_yaml['odom_frame_id'])