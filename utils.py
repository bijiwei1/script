#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil

class counter ():
	pass_cnt = 0
	fail_cnt = 0
	total_cnt = 0


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
		        p1 =subprocess.call(['simv', args1, args2, args3],cwd=tabby , stderr = output, stdout = output, timeout = 60)
			print(testName + " FINISHED")
	            except OSError:
		        print ("Failed test running")
		    except TimeoutExpired:
		    	print testName, 'TIMEOUT'
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

#check all tests in current folder
def check_all_tests (root,testFolder,mode):
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir):
	  	check_test(testDir,x, mode)		 
	else:
		check_all_tests(currDir,x ,mode)
   return


#check  all tests in current folder
def check_all_tests (root,testFolder,mode):
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir):
	  	check_test(testDir,x,mode)		 
	else:
		check_all_tests(currDir,x ,mode)
   return


#simulate specific test in current folder 
def check_unit_test (root, testFolder, testName, mode):   
   currDir = os.path.join(root, testFolder)
   subdir = [dY for dY in os.listdir(currDir) if os.path.isdir(os.path.join(currDir,dY))] 	
   for x in subdir:
	if x == '.git':
		print 'found a git'
		continue	
   	testDir = os.path.join(currDir,x)+'/' 
	print 'current folder:', testDir 
	
	if find_folder(testDir) and x == testName:
	  	check_test(testDir,x,mode)		 
	else:
		check_unit_test(currDir,x ,testName, mode)
   return

def check_test (testDir,testName, mode):
		outPath = testDir + 'out/'
                simFile = outPath+ 'mpu_sim_result'
	     	coreFile = outPath + 'core_result'
                compFile = outPath + 'compare_result'
		#check if out folder exist or not
                if not os.path.exists(outPath):
   	           os.mkdir(outPath)
	
		#check if both files for simulator and our core exists
		if not os.path.exists(simFile):
		   print "Result from simulator doesn't exist"

		if not os.path.exists(coreFile):
		   print "Result from core doesn't exist"
		
		if os.path.exists(compFile):
		   os.remove(compFile)

		f3 = open (compFile, 'w')   #file records result from comparison

		f1 = open (coreFile, 'r')
		f2 = open (simFile, 'r')
		
		line1 = f1.readline()
		line2 = f2.readline()
		
		beginstr = 'core   0: 0x0000000000000200'
		endstr = '(0x0000006f)'

		#find the line where instruction starts
		while (beginstr not in line1):
			line1 = f1.readline()
		
		while (endstr not in line2):
			if (not comp_line(mode, line1, line2)):
				f3.write ("Failed")
				print testName, ' has already been checked and FAILED'
				counter.fail_cnt = counter.fail_cnt + 1;
				counter.total_cnt = counter.total_cnt + 1;
				return;	
			line1 = f1.readline()
			line2 = f2.readline()
	
		f3.write("Passed")
		print testName, ' has already been checked and PASSED'
		counter.pass_cnt = counter.fail_cnt + 1;
		counter.total_cnt = counter.total_cnt + 1;
		return 


def comp_line (mode, l1, l2):
	if mode == '64':
		return l1 == l2

	#check only lower 32 bits
	if ('core' not in l1):
	        s1 = l1.split()
       		s2 = l2.split()
		i =0
		for x in s1:
		   	if i == len(s1)-1:
		       	   immd1 = s1[len(s1)-1][10:] 
			   immd2 = s2[len(s1)-1][10:]
			   if immd1 != immd2:
				  return False
		      	elif x != s2[i]:
			   return False
			else:
			     i = i+1
		return True
	else:
		return l1 == l2 
					

