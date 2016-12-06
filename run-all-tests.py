#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil



inRoot = '/scratch/jiwei/proximate-tests/unit_tests/'
outRoot = '/scratch/jiwei/proximate-tests/unit_tests/'
tabby = '/scratch/jiwei/tabby/src/tb/'

if not os.path.exists(inRoot):
   print ("Test folder doesn't exist")
   quit()

	
subdir = [dI for dI in os.listdir(inRoot) if os.path.isdir(os.path.join(inRoot,dI))] 	

for x in subdir:
      testDir = os.path.join(inRoot,x) + '/'
      outPath = testDir + 'bin/'
      outFile = outPath+ 'core_result'
      #check if bin folder exist or not
      if not os.path.exists(outPath):
   	os.mkdir(outPath)
	
      #remove output files in bin folder	
      try:
    	os.remove(outFile)
      except OSError:
     	pass  
      
      try:
    	os.remove(outPath+'bare_stat.cvs')
      except OSError:
     	pass  
      
      try:
         p1 =subprocess.call(['make'], cwd=testDir)
      except:
         print("Test has problem") 
         quit()

      print 'Running test:',testDir
      args1 = '+TEST=bare'
      args2 = '+IN=' +testDir
      args3 = '+OUT='+outPath
      with open(outFile, "w") as output:
	p1 =subprocess.call(['simv', args1, args2, args3],cwd=tabby , stderr = output, stdout = output)
	print(x + " FINISHED")

print("All test finished")
sys.exit()
