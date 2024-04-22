import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)
	
def sline(argvs):
     
     scommand("objdump  -M intel -d -S $1 ".replace("$1",argvs))
				
     
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="":
	sline(sys.argv[1])
