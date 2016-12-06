import subprocess 
import os
import sys
import shutil

inPath = 'tests/'
outPath = 'results/'
simPath =  '/scratch/jiwei/mpu-riscv/src/'
for filename in os.listdir(inPath):
	simOut ='/scratch/jiwei/tabby/src/tb/'+ outPath+filename+ '_sim'
	simTest = inPath+ filename
	shutil.copyfile (simTest, simPath+'bare')
	with open(simOut, "w") as f:
		p = subprocess.call(['mpu_riscv_sim'],cwd = simPath, stderr = f, stdout = f)
	print(filename + "_SIM FINISHED\n")


print ("All test finished by simulator")
