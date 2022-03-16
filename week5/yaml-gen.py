import os
import pprint
import yaml
import json

from sys import argv


# The same func as dir_through, but for every part of the result of dirlist,
# it writes the data in the yaml file
# It's done to prevent the situation, when the script crashes and all unwritten in the
# file data dissappears
def outro_dir_through(path_: str, dirname: str):
    n_path = os.path.join(path_, dirname)
    dir_list = os.listdir(n_path)
    for content in dir_list:
        n_dict_part = {}
        content_path = os.path.join(n_path, content)
        if os.path.isdir(content_path):
            dir_through(n_path, content, n_dict_part)
        else:
            with open(content_path, 'r') as f:
                try:
                    # yaml.safe_load also reads json content, so, I think,
                    # there is no need in parsing file with json.load()
                    loaded_f = yaml.safe_load(f)
                    # the safe_load here is used only for checking the file
                    # for appropriate content in it.
                    if loaded_f:
                        n_dict_part[content] = [loaded_f]
                except:
                    pass
        with open('yaml_listdir.yaml', 'a+') as f:
            if n_dict_part:
                yaml.dump(n_dict_part, f, default_flow_style=False)


def dir_through(path_: str, dirname: str, dict_part: dict):
    dict_part[dirname] = {}
    n_path = os.path.join(path_, dirname)
    n_dict_part = dict_part[dirname]
    dir_list = os.listdir(n_path)
    for content in dir_list:
        content_path = os.path.join(n_path, content)
        if os.path.isdir(content_path):
            dir_through(n_path, content, n_dict_part)
        else:
            with open(content_path, 'r') as f:
                try:
                    loaded_f = yaml.safe_load(f)
                    if loaded_f:
                        n_dict_part[content] = [loaded_f]
                except:
                    pass


dir_path = argv[1]
path_, _, dirname = dir_path.rpartition('\\')
outro_dir_through(path_, dirname)

# python yaml-gen.py D:/PycharmProjects/MyBooks/instinctools_GA/week5
