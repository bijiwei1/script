#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil

from utils import run_all_tests

os.environ["TESTPATH"]
os.environ["COREPATH"] 
inRoot = os.environ["TESTPATH"]
outRoot =  os.environ["TESTPATH"]
tabby = os.environ['COREPATH']

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
if not os.path.isfile(tabby+ 'simv'):
   print ("You did not setup COREPATH or your COREPATH is not valid")
   quit()

for x in testSet:
   if x == '.git':
      print 'found a git'
      continue	
   run_all_tests(inRoot, x, tabby)


print("All test finished")
sys.exit()
