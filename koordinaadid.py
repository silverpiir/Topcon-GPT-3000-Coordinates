import tkinter as tk
from tkinter import Menu, Tk, ttk
from tkinter.filedialog import askopenfilename
import ntpath

def open_file():
    nimi = askopenfilename(initialdir="/",
                           filetypes = (("Text File", "*.txt"),("All Files","*.*")),
                           title = "Vali lähtefail."
                           )
    global sisendi_read
    global valjundi_nimi
    
    valjundi_nimi = ntpath.basename(nimi)
    sisend = open(nimi, "r", encoding = "UTF-8")
    sisendi_read = sisend.read().splitlines()
    
    #sisendi_read on mälus järjendi kujul, seda näitab järgmine print()
    #print(sisendi_read)
    
    sisend.close()
    silt1 = tk.Label(window, text = nimi)
    silt1.pack()
    
def add_values():
    asi1 = (entry1.get())
    asi2 = (entry2.get())
        
    valjund = open("uus_" + valjundi_nimi, "w")
    
    for rida in sisendi_read:
        if len(rida) > 0:
            #print(rida)
            osad = rida.split(',')
            osad[1] = asi1 + osad[1]
            osad[2] = asi2 + osad[2]
            valjund.write("{}".format(",".join(osad)))
            valjund.write("\n")
    valjund.close()
                
    silt2 = tk.Label(window, text = "Loodud programmiga samas kaustas " + "uus_" + valjundi_nimi)
    silt2.pack()

# Järgneb kasutajaliidese akna kood
window = tk.Tk()

window.title("Topcon GT-3000 koordinaadiprogramm")
window.geometry("500x300")
#window.wm_iconbitmap("prog.ico") ### Toimib, kui on samas kaustas prog.ico

label1 = tk.Label(window, text = "X - koordinaat", font = ("Helvetica", 12))
label2 = tk.Label(window, text = "Y - koordinaat", font = ("Helvetica", 12))
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
nupp = tk.Button(window, text = "Lisa väärtused", command = add_values, width = 20)

label1.pack(pady = 10)
entry1.pack(pady = 2)
label2.pack(pady = 10)
entry2.pack(pady = 2)
nupp.pack(pady = 10)

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff = False)

fileMenu.add_command(label = "Open Source File", command= open_file)
fileMenu.add_command(label = "Exit", command = window.destroy)
menubar.add_cascade(label = "Options", menu = fileMenu)

window.mainloop()
