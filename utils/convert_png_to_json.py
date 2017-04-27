# Usage: python3 convert_png_to_json.py -i input.png -o output.json
# Example: python3 convert_png_to_json.py -i '../images/mario_normal.png' -o 'mario_normal.json'
import argparse

import png
from itertools import zip_longest
import json

# *TODO* Put in wpm as function, or different class. Use JSON to store and load data
# Variables
args = None

def parse_arguments():
    """Parse arguments provided
    return: None
    """
    global args

    parser = argparse.ArgumentParser(description='Convert png to json file')
    parser.add_argument('-i', '--input', action="store", dest="input_filename", type=str, required=True)
    parser.add_argument('-o', '--output', action="store", dest="output_filename", type=str, required=True)
    args = parser.parse_args()
    return None

def read_png(input_filename):
    """Read png file
    return: None
    """
    print("Reading: %s" % input_filename)
    reader = png.Reader(filename=input_filename)
    width, height, pixels, metadata = reader.asRGBA()
    return width, height, pixels, metadata

def grouper(n, iterable, fillvalue=None):
  "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
  args = [iter(iterable)] * n
  return zip_longest(fillvalue=fillvalue, *args)

def process_png(width, height, real_pixels, metadata):
    """Assuming 8 bits = 256 different colors
    Each pixel is R,G,B,A from 0 to 255
    return: width, height, pixels, metadata
    """
    processed_data = {}
    pixel_list = []

    print("Processing pixels with %dx%d" % (width, height))

    # Print metadata info
    if metadata['alpha']:
        print("Using alpha")
    else:
        print("No alpha")

    if metadata['bitdepth']:
        print("bitdepth: %d" % metadata['bitdepth'])

    if metadata['gamma']:
        print("gamma: %d" % metadata['gamma'])

    # Store pixels as hexadecimal
    current_pixel = 0
    counter = 0
    for row in real_pixels:
        for r,g,b,a in grouper(4, row):
            # RGB to hexadecimal
            data = '#%02x%02x%02x' % (r, g, b)
            pixel_list.append(data)

    # Create json from data
    processed_data['width'] = width
    processed_data['height'] = height
    processed_data['metadata'] = metadata
    processed_data['pixel_list'] = pixel_list
    json_data = json.dumps(processed_data)
    return json_data

def save_json(output_filename, json_data):
    print("Saving: %s" % output_filename)
    with open(output_filename, 'w') as outfile:
        json.dump(json_data, outfile)
    return None

if __name__ == "__main__":
    parse_arguments()
    width, height, pixels, metadata = read_png(args.input_filename)
    json_data = process_png(width, height, pixels, metadata)
    save_json(args.output_filename, json_data)
