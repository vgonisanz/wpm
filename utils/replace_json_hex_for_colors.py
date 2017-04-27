# Usage: python3 replace_json_hex_for_colors.py -i input.json
# Example: python3 replace_json_hex_for_colors.py -i 'mario_normal.json' -r '#000000,1;#550000,2;#ffaa55,3;#ff0000,4;'
import argparse

import fileinput

def pair(arg, character = ';'):
    """Assume arg is a pair of strings separated by a character.
    return: tuple
    """
    return [str(x) for x in arg.split(character)]

def parse_arguments():
    """Parse arguments provided
    return: None
    """
    global args

    parser = argparse.ArgumentParser(description='Convert png to json file')
    parser.add_argument('-i', '--input', action="store", dest="input_filename", type=str, required=True)
    parser.add_argument('-r', '--replace', action="store", dest="replace_list", type=pair, nargs='+', required=True)
    args = parser.parse_args()
    #print(args.replace_list)
    return None

def read_json(input_filename):
    """Parse arguments provided
    return: None
    """
    with open(input_filename, 'r') as file:
      file_data = file.read()
    return file_data

def replace_values(file_data, values):
    for value in values:
        if value:
            search_value, replace_value = value.split(',')
            file_data = file_data.replace(search_value, replace_value)
    return file_data

def write_json(output_filename, file_data):
    """Parse arguments provided
    return: None
    """
    with open(output_filename, 'w') as file:
      file.write(file_data)
    return None

if __name__ == "__main__":
    parse_arguments()
    file_data = read_json(args.input_filename)
    file_data = replace_values(file_data, args.replace_list[0])
    write_json(args.input_filename, file_data)
