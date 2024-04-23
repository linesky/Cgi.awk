import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)

def slines1(argvs):
     lst1=[]
     f1=open("/tmp/out.txt","r")
     f2=open("/tmp/out.asm","w")
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
     inss1=None
     inss2=None
     inss3=None
     inss=None
     ina=None
     inaa=None
     inaaa=None
     txx=""
     xtxt1=""
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 f2.write("\n")
                 f2.write(n+"\n")
         else:
             inss1=n.find(":")
             
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]

              	xtxt=n.split("	")
              	n1=0
              	if len(xtxt)>2:
              	    xtxt1=xtxt[2]
              	ina=xtxt1.find("jne ")
              	if ina<0:
              	    ina=xtxt1.find("je ")
              	if ina<0:
              	    ina=xtxt1.find("jnz ")
              	if ina<0:
              	    ina=xtxt1.find("jz ")
              	if ina<0:
              	    ina=xtxt1.find("jng ")  
              	if ina<0:
              	    ina=xtxt1.find("jg ") 
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jo ") 
              	if ina<0:
              	    ina=xtxt1.find("je ")
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jne ")
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jb ") 
              	if ina<0:
              	    ina=xtxt1.find("jnb ") 
              	if ina<0:
              	    ina=xtxt1.find("jl ")
              	if ina<0:
              	    ina=xtxt1.find("jle ")
              	if ina<0:
              	    ina=xtxt1.find("jnl ")
              	if ina<0:
              	    ina=xtxt1.find("jg ")
              	if ina<0:
              	    ina=xtxt1.find("jg ")
              	if ina<0:
              	    ina=xtxt1.find("jng ")
              	if ina<0:
              	    ina=xtxt1.find("jc ")
              	if ina<0:
              	    ina=xtxt1.find("jb ")
              	if ina>-1:
              	    inaa=xtxt1.find("0x")
              	    if inaa>-1:
              	        txx=xtxt1
              	        inaaa=xtxt1.find("0x")
              	        if inaaa<0:
              	            inaaa=len(xtxt1)
              	        txx=txx[inaa:]
              	        txx=txx.strip()
              	        txx=txx.replace("<","")
              	        txx=txx.replace(">","")
              	        lst1=lst1+[txx]             	
              	if len(xtxt)>1:
              	    f2.write("        ")
              	    for nnn in xtxt:
              	        if n1>1:
              	            inss2=nnn.find(" <")
              	            if inss2>-1:
              	                inss3=nnn.find("   ")
              	                nnn=nnn[:inss3]+nnn[inss2:]
              	                nnn=nnn.replace("<","")
              	                nnn=nnn.replace(">","")
              	            f2.write(nnn+" ")		
              	        n1+=1
              	    f2.write("\n")
     f2.close()
     scommand("printf " " > outs.txt ")       	
     for mmm in lst1:
         print(mmm)
         scommand("objdump -M intel -D -b binary --start-address=$1 -mi386 -Maddr32,data32 /tmp/out.bin".replace("$1",mmm))
     
	
def sline(argvs1,argvs2):
     lst1=[]
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
     ina=None
     inaa=None
     inaaa=None
     txx=""
     xtxt1=""
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
              	if len(xtxt)>2:
              	    xtxt1=xtxt[2]
              	

              	n1=0     
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
     scommand("objdump -M intel -D -b binary -mi386 -Maddr32,data32 /tmp/out.bin> out.txt")        	   
     slines1("")
     scommand("cat /tmp/out.asm")
     scommand("cat /tmp/outs.asm")      	
	
print("\x1bc\x1b[43;37m")	
if sys.argv[1]!="" and sys.argv[2]!="":
	sline(sys.argv[1],sys.argv[2])
