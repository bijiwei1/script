#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil


#find the folder in the botton level where all tests are 
def find_folder (currdir):
   subdir = [dY for dY in os.listdir(currdir) if os.path.isdir(currdir)] 	
   for x in subdir:
      item = os.path.join(currdir,x) 
      if os.path.isdir(item) and (x != 'bin') and (x!='out'):
	 return False
   return True
      	 

#run all tests in current folder
def run_all_tests (root,testFolder,tabby):
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir):
	  	run_test(testDir,x,tabby)		 
	else:
		run_all_tests(currDir,x ,tabby)
   return

#run specific test in current folder 
def run_unit_test (root, testFolder, tabby, testName):   
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir) and x == testName:
	  	run_test(testDir,x,tabby)		 
	else:
		run_unit_test(currDir,x ,tabby, testName)
     
   return


def run_test (testDir,testName,tabby):
	         outPath = testDir + 'out/'
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
	            try:
		        p1 =subprocess.call(['simv', args1, args2, args3],cwd=tabby , stderr = output, stdout = output)
			print(testName + " FINISHED")
	            except OSError:
		        print ("Failed test running")

		 return 


#simulate all tests in current folder
def sim_all_tests (root,testFolder,simPath):
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir):
	  	sim_test(testDir,x,simPath)		 
	else:
		sim_all_tests(currDir,x ,simPath)
   return


#simulate specific test in current folder 
def sim_unit_test (root, testFolder, simPath, testName):   
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir) and x == testName:
	  	sim_test(testDir,x,simPath)		 
	else:
		sim_unit_test(currDir,x ,simPath, testName)
   return


	
def sim_test (testDir,testName, simPath):
	         outPath = testDir + 'out/'
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
                 shutil.copyfile (testDir + 'bare', simPath + 'bare')
		 with open(outFile, "w") as output:
	            try:
		        p1 =subprocess.call(['mpu_riscv_sim'],cwd=simPath, stderr = output, stdout = output)
			print(testName + " SIMULATE FINISHED")
	            except OSError:
		        print ("Failed test running")

		 return 


