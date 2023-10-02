import os
import tkinter as tk

from whiteboard.app import Whiteboard
from whiteboard.ui import get_image_folder


def main():
    root = tk.Tk()
    Whiteboard(root)
    root.geometry("1050x570+150+50")
    # Establece el icono de la aplicación
    icon_path = os.path.join(get_image_folder(), 'logo.png')
    root.iconbitmap(icon_path)
    root.iconphoto(False, tk.PhotoImage(file=icon_path))
    root.resizable(True, True)
    root.mainloop()


if __name__ == "__main__":
    main()
