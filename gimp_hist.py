#!/usr/bin/python
import os,sys
from gimpfu import *

def calculate_histogram(filename):
    img = load_image(filename)
    layers = img.layers
    drw = layers[len(layers) - 1]
    ch = HISTOGRAM_VALUE # can be other value such as _RED, _GREEN,ETC..
    start_intensity = .0
    end_intensity = 1.0
    intensity_histogram = pdb.gimp_drawable_histogram(drw, ch, start_intensity, end_intensity)
    # intensity_histogram[0] / 255 must be computed later
    return intensity_histogram

def load_image(file):
    fn = find_image_type(file)
    return fn(file, 1)

def select_region(img, x, y, w, h):
    # select specific region prior to getting the histogram
    # useful when we have a large canvas such as dual monitors 
    pbd.gimp_image_select_rectangle(img, x, y, w, h)


def find_image_type(file):
    fn = None
    if(file[-3:].endswith("png")):
        fn = pdb.file_png_load
    elif(file[-3:].endswith("jpg")):
        fn = pdb.file_jpg_load
    elif(file[-3:].endswith("bmp")):
        fn = pdb.file_bmp_load

    return fn

if __name__ == "__main__":
    
    for filename in os.listdir(os.getcwd()):
        try:
            (f,ext) = filename.split(".")
            if ext in ["jpg", "png", "bmp"]:
                intensity = calculate_histogram(filename)
                print(intensity)
        except:
            print("error: ", filename)
            pass
