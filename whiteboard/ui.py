import tkinter as tk
from tkinter import ttk
import sys
import os


def get_image_folder():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'icons')
    else:
        return 'icons'


def create_widgets(self):
    self.slider = ttk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.slider_changed)
    self.slider.place(x=30, y=530)

    self.value_label = ttk.Label(self.root, text=self.get_current_value())
    self.value_label.place(x=27, y=550)

    # Usa la ruta de la carpeta de imágenes determinada según el entorno
    eraser_icon = os.path.join(get_image_folder(), 'eraser.png')
    self.eraser = tk.PhotoImage(file=eraser_icon)
    tk.Button(self.root, image=self.eraser, bg="#f2f3f5", command=self.new_canvas, bd=0, activebackground="#f2f3f5",
              cursor="hand2").place(x=30, y=400)

    import_image_icon = os.path.join(get_image_folder(), 'addimage.png')
    self.import_image = tk.PhotoImage(file=import_image_icon)
    tk.Button(self.root, image=self.import_image, bg="white", bd=0, activebackground="#f2f3f5", cursor="hand2",
              command=self.insert_image).place(x=30, y=450)


def bind_events(self):
    self.canvas.bind('<Button-1>', self.locate_xy)
    self.canvas.bind('<B1-Motion>', self.add_line)
