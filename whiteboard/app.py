import os
import tkinter as tk
from tkinter import filedialog
from whiteboard.ui import create_widgets, bind_events
from whiteboard.utils import load_image


class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizarra")
        self.root.config(bg="#f2f3f5")

        # Crear un frame principal que ocupará todo el espacio disponible
        main_frame = tk.Frame(self.root, bg="#f2f3f5")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Configurar el sistema de geometría para que sea responsivo
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Crear el canvas en el lado derecho
        self.canvas = tk.Canvas(main_frame, background="white", cursor="pencil")
        self.canvas.grid(row=0, column=1, sticky=tk.NSEW, padx=(10, 0))
        self.canvas.bind("<Configure>", self.canvas_resized)  # Manejar el evento de redimensionamiento del canvas
        self.current_x = 0
        self.current_y = 0
        self.color = "black"
        self.value_label = None
        self.slider = None
        self.filename = None
        self.setup_ui()

        # Crear el sidebar en el lado izquierdo
        sidebar = tk.Frame(main_frame, bg="#f2f3f5")
        sidebar.grid(row=0, column=0, sticky=tk.NS)
        sidebar.grid_columnconfigure(0, weight=1)

    def setup_ui(self):
        create_widgets(self)
        bind_events(self)
        self.display_pallet()

    def canvas_resized(self, event):
        """Ajusta el tamaño del canvas cuando cambie el tamaño de la ventana"""
        self.canvas.config(width=event.width, height=event.height)

    def insert_image(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecciona un archivo", filetypes=(
            ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
        load_image(self.canvas, self.filename)

    def locate_xy(self, event):
        self.current_x = event.x
        self.current_y = event.y

    def add_line(self, event):
        self.canvas.create_line((self.current_x, self.current_y, event.x, event.y), fill=self.color,
                                width=self.get_current_value(), capstyle=tk.ROUND, smooth=True)
        self.current_x = event.x
        self.current_y = event.y

    def slider_changed(self, event):
        self.value_label.configure(text=self.get_current_value())

    def get_current_value(self):
        return '{: .2f}'.format(self.slider.get())

    def show_color(self, new_color):
        self.color = new_color

    def new_canvas(self):
        self.canvas.delete("all")
        self.display_pallet()

    def display_pallet(self):
        colors = tk.Canvas(self.root, bg="#fff", width=37, height=300, bd=0)
        colors.place(x=30, y=60)

        color_list = ["black", "gray", "brown4", "red", "orange", "yellow", "green", "blue", "purple"]
        for i, color in enumerate(color_list):
            _id = colors.create_rectangle(10, 10 + 30 * i, 30, 30 + 30 * i, fill=color)
            colors.tag_bind(_id, "<Button-1>", lambda x, c=color: self.show_color(c))
