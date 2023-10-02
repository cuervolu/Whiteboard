import os
import tkinter as tk
from tkinter import Text, Scrollbar
from ttkthemes import ThemedStyle


def show_error_details(exception_message):
    # Crea una nueva ventana para mostrar los detalles de la excepción
    error_window = tk.Toplevel()
    error_window.title("Detalles del Error")

    # Utiliza un estilo de tema "equilux" de ttkthemes para mejorar la apariencia
    style = ThemedStyle(error_window)
    style.set_theme("elegance")

    # Crea un widget Text para mostrar los detalles de la excepción con el estilo temático
    error_text = Text(error_window, wrap=tk.WORD, height=15, width=50)
    error_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Agrega una barra de desplazamiento al widget Text
    scrollbar = Scrollbar(error_text)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    error_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=error_text.yview)

    # Inserta el mensaje de la excepción en el widget Text
    error_text.insert(tk.END, exception_message)


def load_image(canvas, filename):
    global f_img
    valid_extensions = (".png", ".jpg", ".jpeg")
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension not in valid_extensions:
        # Muestra un mensaje de error personalizado con botón "Ver detalles"
        error_message = "Formato de archivo no válido. Selecciona un archivo de imagen válido."
        show_custom_error_message(error_message, False)
        return

    try:
        global f_img
        f_img = tk.PhotoImage(file=filename)
        my_img = canvas.create_image(180, 50, image=f_img)
        bind_mouse_motion(canvas, filename)
        canvas.update()
    except Exception as e:
        print(f"Error loading image: {e}")
        # Muestra un mensaje de error personalizado con botón "Ver detalles"
        error_message = "No se pudo cargar la imagen."
        show_custom_error_message(error_message)


def bind_mouse_motion(canvas, filename):
    canvas.bind("<B3-Motion>", lambda event, c=canvas, f=filename: my_callback(event, c, f))


def my_callback(event, canvas, filename):
    global f_img
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x, event.y, image=f_img)


def show_custom_error_message(message, show_details_button=True):
    custom_error_window = tk.Toplevel()
    custom_error_window.title("Error")

    style = ThemedStyle(custom_error_window)
    style.set_theme("elegance")

    error_label = tk.Label(custom_error_window, text=message)
    error_label.pack(padx=10, pady=10)

    ok_button = tk.Button(custom_error_window, text="Aceptar", command=custom_error_window.destroy)
    ok_button.pack(side=tk.LEFT, padx=5)

    if show_details_button:
        details_button = tk.Button(custom_error_window, text="Ver detalles",
                                   command=lambda: show_error_details(message))
        details_button.pack(side=tk.RIGHT, padx=5)

    # Hacer que la ventana se destruya automáticamente al cerrarse
    custom_error_window.protocol("WM_DELETE_WINDOW", custom_error_window.destroy)

    custom_error_window.mainloop()
