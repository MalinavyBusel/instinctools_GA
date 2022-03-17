import os
import pprint
import yaml
import json


def path_file_gener(data_path: str, dir_name: str = 'restored_data'):
    with open(data_path, 'r') as f:
        my_file = yaml.safe_load(f)
    checker(my_file, 'restored')


def checker(data_dict: dict, dir_name: str):
    os.mkdir(dir_name)
    for key, value in data_dict.items():
        n_dir_name = os.path.join(dir_name, key)

        if type(value) == dict:
            checker(data_dict[key], n_dir_name)

        else:
            with open(n_dir_name, 'w') as f:
                if value[0] == 'yaml':
                    yaml.dump(value[1], f, default_flow_style=False)
                else:
                    json.dump(value[1], f)


path_file_gener('yaml_listdir.yaml')
