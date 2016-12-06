#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil


try:
   test = sys.argv[1]
except IndexError:
   print("Did not enter an unit test")
   quit()

inRoot = '/scratch/jiwei/proximate-tests/unit_tests/'
outRoot = '/scratch/jiwei/proximate-tests/unit_tests/'

if not os.path.exists(inRoot):
   print ("Test folder doesn't exist")
   quit()

subdir = [dI for dI in os.listdir(inRoot) if os.path.isdir(os.path.join(inRoot,dI))] 	

for x in subdir:
   if x == test:
      testPath = os.path.join(inRoot,test)
      print 'Running test:',testPath
      args1 = '+TEST='
      args2 = '+IN='+inPath
      args3 = '+OUT='+outPath
      outFile = outPath+filename
      with open(outFile, "w") as output:
		p1 =subprocess.call(['simv', args1, args2, args3], stderr = output, stdout = output)
	print(filename + " FINISHED")

           
