import png
from itertools import zip_longest

# Variables
input_filename = '../images/mario_normal.png'
output_filename = 'mario_normal.txt'

def read_png(input_filename):
    print("Reading: %s" % input_filename)
    # Read PNG
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
    color_id = []
    tuple_size = 3
    print("Processing pixels with %dx%d" % (width, height))

    # Check alpha
    if metadata['alpha']:
        print("Using alpha")
        tuple_size = 4
    else:
        print("No alpha")
        tuple_size = 3

    if metadata['bitdepth']:
        print("bitdepth: %d" % metadata['bitdepth'])

    if metadata['gamma']:
        print("gamma: %d" % metadata['gamma'])

    current_pixel = 0
    counter = 0
    for row in real_pixels:
        for r,g,b,a in grouper(4, row):
            # RGB to hexadecimal
            data = '#%02x%02x%02x' % (r, g, b)
            color_id.append(data)
    return color_id

def save_data(output_filename, real_color_id, width, height):
    print("Processing: %s" % output_filename)
    output_file = open(output_filename, "w")
    for i in range(0, height):
        output_file.write("\nRow %d: " % i)
        for j in range(0, width):
            index = j + i * width
            data = real_color_id[index]
            #print("%d " % data)
            if j == width - 1:
                output_file.write("%s" % data)
            else:
                output_file.write("%s," % data)
    output_file.close()
    return None

if __name__ == "__main__":
    width, height, pixels, metadata = read_png(input_filename)
    color_id = process_png(width, height, pixels, metadata)
    save_data(output_filename, color_id, width, height)
