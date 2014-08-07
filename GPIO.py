import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

BOARD = 0
OUT = 0

cubeRefs = np.meshgrid(range(0,5),range(0,5),range(0,5))

def setmode(i):
	print "mode set"

def setup(i,j):
	print "pin setup"

def output(i,j):
	pass


def display(cube):
	print cube.lattice