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
     f1=open("/tmp/out.asm","w")
     f1.write("[bits 32]\n")
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 f1.write("\n")
                 f1.write(n+"\n")
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
              	               f1.write("db 0x")
              	        else:
              	           if tx!="":           	        
              	               f1.write(",0x")
              	        if tx!="":  
              	            f1.write(tx)
              	        counts+=1
              	    f1.write("\n")
     f1.close()            	    
     scommand("nasm -f bin /tmp/out.asm -o /tmp/out.bin")
     scommand("objdump -M intel -D -b binary -mi386  -Maddr32,data32 /tmp/out.bin")        	   
              	
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="" and sys.argv[2]!="":
	sline(sys.argv[1],sys.argv[2])
