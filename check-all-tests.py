#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil

from utils import check_all_tests
from utils import counter


try:
   mode = sys.argv[1]
except IndexError:
   print("Did not choose 64 or 32 bit")
   quit()

os.environ["TESTPATH"]
inRoot = os.environ["TESTPATH"]
outRoot =  os.environ["TESTPATH"]

if not os.path.exists(inRoot):
   print ("Test folder doesn't exist")
   quit()

#check if testpath is correct or not	
try:
   testSet = [dI for dI in os.listdir(inRoot) if os.path.isdir(os.path.join(inRoot,dI))] 	
except OSError:
   print ("You did not setup TESTPATH or your TESTPATH is not valid")
   quit()

for x in testSet:
   if x == '.git':
      print 'found a git'
      continue	
   check_all_tests(inRoot,x, mode)

print 'Finish checking all test'	
print 'Summary: Total test: ', counter.total_cnt, ' Passed tests: ', counter.pass_cnt, ' Failed tests: ', counter.fail_cnt


sys.exit()
