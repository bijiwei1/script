#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil
from utils import sim_unit_test


try:
   testName = sys.argv[1]
except IndexError:
   print("Did not enter an unit test")
   quit()

os.environ['TESTPATH']
os.environ['SIMPATH']

inRoot = os.environ["TESTPATH"]
outRoot =  os.environ["TESTPATH"]
simPath= os.environ['SIMPATH']

if not os.path.exists(inRoot):
   print ("Test folder doesn't exist")
   quit()

#check if testpath is correct or not	
try:
   testSet = [dI for dI in os.listdir(inRoot) if os.path.isdir(os.path.join(inRoot,dI))] 	
except OSError:
   print ("You did not setup TESTPATH or your TESTPATH is not valid")
   quit()

#check if corepath is correct or not	
if not os.path.isfile(simPath+ 'mpu_riscv_sim'):
   print ("You did not setup SIMPATH or your SIMPATH is not valid")
   quit()

for x in testSet:
   if x == '.git':
      print 'found a git'
      continue	
   sim_unit_test(inRoot, x, simPath,testName)

sys.exit()
