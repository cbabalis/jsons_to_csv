""" This module collects all json data to a single dictionary and
it writes it to a csv file.
"""

import json
import os
from flatten_json import *


def get_json_file_list(folder="data"):
    """ method to return a list full of json files."""
    json_file_list = []
    for file in os.listdir(folder):
        if file.endswith(".json"):
            json_file_list.append(os.path.join(folder, file))
    return json_file_list


def create_dict_keys_from_json(json_file):
    """ method to create a *flat* dictionary out of a json file."""
    data = json.load(open(json_file))
    my_dict = flatten_json_iterative_solution(data)
    return my_dict


def replace_value_with_list_inside_value(big_dic):
    """ this method replace the value of a dictionary with a list
    which contains its value.
    """
    for key, value in big_dic.items():
        big_dic[key] = [value]


def populate_big_dictionary(big_dic, json_file_list):
    """ This method merges the json files to a big dictionary.
    This is happening as follow:
    1. Read the json files one each time and create a dictionary.
    2. Compare the keys of the newly created dictionary to the ones of
        the big dictionary.
    3. If it is a hit, then populate a list that corresponds to the key
        with new data, else populate it with 0.
    """
    for a_file in json_file_list:
        a_dic = create_dict_keys_from_json(a_file)
        merge_dictionaries(big_dic, a_dic)


def merge_dictionaries(big_dic, dic):
    """ method to append the values of the dic to the big_dic."""
    for key in big_dic.keys():
        if key in dic:
            big_dic[key].append(dic[key])
        else:
            big_dic[key].append(0)


def main():
    # read all files
    json_file_list = get_json_file_list()
    # create a big dictionary and populate it with the rows.
    # do that by popping out the first item of the list and
    # by using it in order to populate the new dictionary.
    json_file = json_file_list.pop(0)
    big_dic = create_dict_keys_from_json(json_file)
    replace_value_with_list_inside_value(big_dic)
    # add data from each file
    populate_big_dictionary(big_dic, json_file_list)
    print(big_dic)
    # write the big dictionary to a csv


if __name__ == "__main__":
    main()
