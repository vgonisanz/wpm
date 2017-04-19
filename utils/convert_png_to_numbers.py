import png

# Read PNG
reader = png.Reader(filename='../images/mario_normal.png')
width, height, pixels, metadata = reader.read_flat()

# Check alpha
if metadata['alpha']:
    print("Using alpha")
    pixel_byte_width = 4
else:
    print("No alpha")
    pixel_byte_width = 3

print("Colors are:")
current_pixel = 0
for i in range(0, height):
    print("\nPixel row: ")
    for j in range(0, width):
        index = j * width + i
        initial = 0
        if pixel_byte_width == 4:
            initial = 1
        color_id = pixels[index + initial] +  pixels[index + initial + 1] +  pixels[index + initial + 2]
        print("[%s]" % color_id)
