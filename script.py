#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil



inPath = 'tests/'
outPath = 'results/'
simPath =  '/scratch/jiwei/mpu-riscv/src/'
if not os.path.exists(inPath):
	print("Test folder doesn't exist")
	quit()

if not os.path.exists(outPath):
	os.makedirs(outPath)

for filename in os.listdir(inPath):
	args1 = '+TEST='+filename
	args2 = '+IN='+inPath
	args3 = '+OUT='+outPath
	outFile = outPath+filename
	with open(outFile, "w") as output:
		p1 =subprocess.call(['simv', args1, args2, args3], stderr = output, stdout = output)
	print(filename + " FINISHED")

print("Finished all tests in tabby")
	

