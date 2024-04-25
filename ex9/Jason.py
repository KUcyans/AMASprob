######################################################################
# D. Jason Koskinen
# April 29, 2016
#
# So this is the code to check the students
# submissions for their classification algorithms
# for the cancer question on the 2016 exam for
# Advanced Methonds in Applied Statistics
######################################################################

from array import array
import io
import numpy
import os
import root_numpy as rnp

import random
import ROOT
from ROOT import *

import sys

savePlots = False


gStyle.SetTitleSize( 0.055,"xyz")
gStyle.SetTitleOffset( 0.66,"xy")
gStyle.SetHistLineWidth( 2)

##############################
# Now check
##############################

lsdir = os.listdir("/Users/koskinen/Documents/Courses/AdvancedMethodsInAppliedStatistics2016/StudentExams/Advanced Methods in Applied Statistics_174202-2")

benign_student_files    = []
malignant_student_files = []

# Look through the list of files from the
# exam submissions and grab those
# that match the file names and file types
# which were explicitly part of the exam
# question for the classification exercise.
# It is not required to use a BDT, but
# the grading is based on the final
# purity in correctly classifying the
# sample as either benign or malignant.

for entry in lsdir:
    if 'BENIGN' in entry.upper():
        benign_student_files.append("/Users/koskinen/Documents/Courses/AdvancedMethodsInAppliedStatistics2016/StudentExams/Advanced Methods in Applied Statistics_174202-2/%s" % entry)
        print entry
    # end if
    if 'MALIGNANT' in entry.upper():
        malignant_student_files.append("/Users/koskinen/Documents/Courses/AdvancedMethodsInAppliedStatistics2016/StudentExams/Advanced Methods in Applied Statistics_174202-2/%s" % entry)
        print entry
    # end if
# end if

infile_mal_true = numpy.loadtxt("data/malignant_true.txt", delimiter = " ")
infile_ben_true = numpy.loadtxt("data/benign_true.txt", delimiter = " ")

for ben, mal in zip( benign_student_files, malignant_student_files):
    print ben

    infile_mal_ID = numpy.loadtxt( mal)
    infile_ben_ID = numpy.loadtxt( ben)

    overlap_mal = numpy.intersect1d(infile_mal_true[0:], infile_mal_ID[0:])
    overlap_ben = numpy.intersect1d(infile_ben_true[0:], infile_ben_ID[0:])

    print "len(infile_mal_true): ", len(infile_mal_true)
    print "len(overlap_mal): ", len(overlap_mal)
    
    print "len(infile_ben_true): ", len(infile_ben_true)
    print "len(overlap_ben): ", len(overlap_ben)

    print "efficiency: ", (len(overlap_mal)+len(overlap_ben))*1.0/(len(infile_mal_true)+len(infile_ben_true))
    print "\n\n"
# end for



raw_input('Press Enter to exit')

