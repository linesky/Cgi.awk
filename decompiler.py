import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)
	
def sline(argvs):
     
     scommand("objdump  -M intel -d -S $1 > /tmp/out.txt".replace("$1",argvs))
     scommand("gedit /tmp/out.txt")			
     
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="":
	sline(sys.argv[1])
