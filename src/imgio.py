import utils.imutils as iu #TODO: make imutils minimal.
import utils.fp as fp
import numpy as np
import cv2
from PyQt5.QtGui import QImage

load = fp.multi(lambda p,s=None: s)
NDARR = 'ndarr'
MASK  = 'mask' 

@fp.mmethod(load, None)
def load(path, type=None): return QImage(path)
@fp.mmethod(load, NDARR)
def load(path, type): return iu.imread(path)
@fp.mmethod(load, MASK)
def load(path, type): return mask2segmap(iu.imread(path))

def segmap2mask(segmap):
    '''
    convert segmap(snet output) to mask(gui, file)

    segmap: np.uint8, bgr,  {fg=white, bg=black}
    mask:   np.uint8, bgra, {fg=red, bg=transparent}
    '''
    _,_,r = cv2.split(segmap) # b=g=r, a=r
    b = g = np.zeros_like(r)
    return cv2.merge((b,g,r,r))

def mask2segmap(mask):
    '''
    convert mask(gui, file) to segmap(snet output) 

    mask:   np.uint8, bgra, {fg=red, bg=transparent}
    segmap: np.uint8, bgr, b=g=r {fg=white, bg=black}
    '''
    return fp.go(
        mask,
        lambda m4: np.sum(m4, axis=-1),
        lambda m1: np.expand_dims(m1, axis=-1),
        lambda m1: cv2.merge((m1,m1,m1))
    )

def save(path, img): #TODO: multimethod..?
    cv2.imwrite(path, img)