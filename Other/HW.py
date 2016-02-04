#! usr/bin/python
import numpy
from statistics import mode

dataFile = open("data.txt", r)

data = dataFile.split()

def Median(df):
    return numpy.median(numpy.array(df))

def Average(df):
    return numpy.average(numpy.array(df))

def Mode(df):
    return mode(df)

statFile = open("stat.txt", w)

statFile.writeLines("Median: " + Median(data) + "\n" + "Mode: " + Mode(data) + "\n" + "Mean: " + Average(data))
