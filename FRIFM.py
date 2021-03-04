'''
Implementation of FRIFM : https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=890059
Created on March 3, 2021 at Oak Ridge National Laboratory
@author: Joel Brogan
'''

import dlib
import numpy as np
from skimage.filters import sobel 
from skimage.transform import rescale
import skimage.io as skio

import os
import sys

def FRIFM(im,det,standardWidth=150):
    chip = im[d.top():d.bottom(),d.left():d.right()]
    chip_width = chip.shape[1]
    scale_factor = standardWidth/chip_width
    chip = rescale(chip,scale_factor,anti_aliasing=False)
    FRIFM = sobel(chip).mean()
    return FRIFM

def runFRIFM(impath,standardWidth=150):
    detector = dlib.get_frontal_face_detector()
    im = (skio.imread(impath,1)*255).astype(np.uint8)
    dets = detector(im)
    FRIFM_array = []
    for d in dets:
        FRIFM_array.append(FRIFM(im,d,standardWidth))
    return FRIFM_array
if __name__ == '__main__': 
    impath = sys.argv[1]
    FRIFM_array = runFRIFM(impath)
    print("Number of faces detected: ", len(FRIFM_array))
    print("FRIFM Values:",FRIFM_array)