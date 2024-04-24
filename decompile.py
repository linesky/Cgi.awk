import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
global sself
def prints(txts:str):
    global sself
    sself.text_area.insert(tk.END,txts )
    
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
     inss2=None
     inss3=None
     inss=None
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 prints(""+"\n")
                 prints(n+"\n")
         else:
             inss1=n.find(":")
             
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]

              	xtxt=n.split("	")
              	n1=0;
              	
              	if len(xtxt)>1:
              	    prints("        ")
              	    for nnn in xtxt:
              	        if n1>1:
              	            inss2=nnn.find(" <")
              	            if inss2>-1:
              	                inss3=nnn.find("   ")
              	                nnn=nnn[:inss3]+nnn[inss2:]
              	                nnn=nnn.replace("<","")
              	                nnn=nnn.replace(">","")
              	            prints(nnn+" ")		
              	        n1+=1
              	    prints("\n")
              	

class BareboneBuilder:
    def __init__(self, root):
        global sself
        sself=self
        i:int=0
        self.root = root
        self.root.title("editor")

        
        
        self.menubar = tk.Menu(self.root)
        self.mainmenu = tk.Menu(self.menubar, tearoff=0)
        
        # Área de texto
        self.text_1 = tk.Text(self.root, height=1, width=80,bg='yellow')
        self.text_1.pack(pady=10)
        self.text_2 = tk.Text(self.root, height=1, width=80,bg='yellow')
        self.text_2.pack(pady=10)

        self.text_area = tk.Text(self.root, height=25, width=80,bg='yellow')
        self.text_area.pack(pady=10)

        # Botões
        self.b1=self.mainmenu.add_command( label="new file", command=self.build_kernel)
        

        self.b2=self.mainmenu.add_command( label="load file", command=self.run_kernel)
        

        self.b3=self.mainmenu.add_command( label="save file", command=self.copy_file)
        self.b12=self.mainmenu.add_command( label="replace", command=self.replaces)
        self.b6=self.mainmenu.add_command( label="exit", command=self.root.quit)
        self.b5=self.menubar.add_cascade(label="main", menu=self.mainmenu)
        
        self.b4=self.root.configure(menu=self.menubar,bg='yellow')
        self.text_1.insert(tk.END,"find" )
        self.text_2.insert(tk.END,"replace" )

    def build_kernel(self):
        
        self.text_area.delete(1.0, tk.END)
    def replaces(self):
        txts=self.text_area.get("1.0", "end-1c")
        txts=txts.replace(self.text_1.get("1.0", "end-1c"),self.text_2.get("1.0", "end-1c"))
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END,txts )
        
        
       
    def run_kernel(self):
        filename = tk.filedialog.askopenfilename(title="load file")
        self.text_area.delete(1.0, tk.END)
        sline(filename)



    def copy_file(self):
        
        heads=self.text_area.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(title="save file")
        f2=open(filename,"w")
        f2.write(heads)
        f2.close()



if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    
    root.mainloop()
