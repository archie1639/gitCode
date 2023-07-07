from tkinter import *
from PIL import Image, ImageTk

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Archie")

        self.image = Image.open("images/logo1.jfif")
        self.icon_title = ImageTk.PhotoImage(self.image)
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

root = Tk()
obj = IMS(root)
root.mainloop()
