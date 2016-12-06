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
simPath =  '/scratch/jiwei/mpu-riscv/src/'

if not os.path.exists(inRoot):
   print ("Test folder doesn't exist")
   quit()

subdir = [dI for dI in os.listdir(inRoot) if os.path.isdir(os.path.join(inRoot,dI))] 	

for x in subdir:
   if x == test:
      testDir = os.path.join(inRoot,test) + '/'
      outPath = testDir + 'bin/'
      outFile = outPath+ 'mpu_sim_result'
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
      shutil.copyfile (testDir+'bare', simPath+'bare')
      with open(outFile, "w") as output:
	p1 =subprocess.call(['mpu_riscv_sim'],cwd=simPath , stderr = output, stdout = output)
	print(test + " FINISHED")

sys.exit()
