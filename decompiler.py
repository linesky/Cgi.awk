import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)
	
def sline(argvs):
     
     scommand("objdump  -M intel -d -S $1 > /tmp/out.txt".replace("$1",argvs))
     f1=open("/tmp/out.txt","r")
     txt=f1.read()
     f1.close()
     txt=txt.replace("\r","\n")
     txt=txt.replace("\n\n","\n")
     
     txtx=txt.split("\n")
     txt=None
     inss1=None
     inss=None
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 print("")
                 print(n)
         else:
             inss1=n.find(":")
             n=n.replace(">","")
             n=n.replace("<","")
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]
              	xtxt=n.split("	")
              	n1=0;
              	if len(xtxt)>1:
              	    print("        ",end="")
              	    for nnn in xtxt:
              	        if n1>1:
              	            print(nnn+" ",end="")		
              	        n1+=1
              	    print("")
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="":
	sline(sys.argv[1])
