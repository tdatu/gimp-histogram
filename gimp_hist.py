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
#    fn = None
#    fn = file[-3:].endswith("png") if pdb.file_png_load else None
#    fn = file[-3:].endswith("jpg") and fn != None if pdb.file_png_load else None
#    fn = file[-3:].endswith("bmp") and fn != None if pdb.file_png_load else None
    return pdb.file_png_load

if __name__ == "__main__":
    filename = "antartica.png"
    intensity = calculate_histogram(filename)
    print(intensity)
