import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)
	
def sline(argvs1,argvs2):
     
     scommand('objdump  -M intel -d -S --disassemble=$2 "$1" > /tmp/out.txt'.replace("$1",argvs1).replace("$2",argvs2))
     f1=open("/tmp/out.txt","r")
     txt=f1.read()
     f1.close()
     txt=txt.replace("\r","\n")
     txt=txt.replace("\n\n","\n")
     
     txtx=txt.split("\n")
     txt=None
     inss1=None
     inss2=None
     inss3=None
     inss=None
     print("[bits 32]")
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
             
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]

              	xtxt=n.split("	")
              	n1=0;
              	
              	if len(xtxt)>1:
              	    txtxx=xtxt[1].split(" ")
              	    if xtxt[1].find("e8 fc ff ff ff")>-1:
              	        txtxx=txtxx[1:]
              	    counts=0
              	    for tx in txtxx:
              	        if counts==0:
              	           if tx!="":
              	               print("db 0x",end="")
              	        else:
              	           if tx!="":           	        
              	               print(",0x",end="")
              	        if tx!="":  
              	            print(tx,end="")
              	        counts+=1
              	    print("")
              	    

              	   
              	
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="" and sys.argv[2]!="":
	sline(sys.argv[1],sys.argv[2])
