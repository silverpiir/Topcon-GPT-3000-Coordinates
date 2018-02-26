import tkinter as tk
from tkinter import Menu, Tk, ttk
from tkinter.filedialog import askopenfilename
import ntpath

def open_file():
    filename = askopenfilename(initialdir="/",
                           filetypes = (("Text File", "*.txt"),("All Files","*.*")),
                           title = "Open Source File"
                           )
    global infile_rows
    global output_name
    
    output_name = ntpath.basename(filename)
    infile = open(filename, "r", encoding = "UTF-8")
    infile_rows = infile.read().splitlines()
    
    infile.close()
    label_1 = tk.Label(window, text = filename)
    label_1.pack()
    
def add_values():
    input_value_x = (entry_x.get())
    input_value_y = (entry_y.get())
        
    outfile = open("new_" + output_name, "w")
    
    for row in infile_rows:
        if len(row) > 0:
            segments = row.split(',')
            segments[1] = input_value_x + segments[1]
            segments[2] = input_value_y + segments[2]
            outfile.write("{}".format(",".join(segments)))
            outfile.write("\n")
    outfile.close()
                
    label_2 = tk.Label(window, text = "new_" + output_name + " created in this program's folder.")
    label_2.pack()

window = tk.Tk()

window.title("Topcon GT-3000 Coordinates Correction")
window.geometry("500x300")
#window.wm_iconbitmap("prog.ico")

label_x = tk.Label(window, text = "X - coordinate", font = ("Helvetica", 12))
label_y = tk.Label(window, text = "Y - coordinate", font = ("Helvetica", 12))
entry_x = tk.Entry(window)
entry_y = tk.Entry(window)
submit_btn = tk.Button(window, text = "Add values", command = add_values, width = 20)

label_x.pack(pady = 10)
entry_x.pack(pady = 2)
label_y.pack(pady = 10)
entry_y.pack(pady = 2)
submit_btn.pack(pady = 10)

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff = False)

fileMenu.add_command(label = "Open Source File", command= open_file)
fileMenu.add_command(label = "Exit", command = window.destroy)
menubar.add_cascade(label = "Options", menu = fileMenu)

window.mainloop()
