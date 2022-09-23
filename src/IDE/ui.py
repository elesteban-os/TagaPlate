import tkinter as tk


class UI:
    root = tk.Tk()
    menu = tk.Menu()
    optionFile = tk.Menu(menu, tearoff=False)
    
    def openFile(self):
        print("Opening file...")

    def __init__(self):
        # Menu
        self.optionFile.add_command(label="New file...", command=self.openFile)

        self.menu.add_cascade(menu=self.optionFile, label="File")


        # Ventana
        self.root.config(width=600, height=600, menu=self.menu)
        self.root.title("IDE")
        self.root.resizable(1, 1)

        self.root.mainloop()


        

ui = UI()


