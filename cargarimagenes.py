import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Asegúrate de tener instalada la biblioteca Pillow

class ImageUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Uploader")

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        browse_button.pack(pady=10)

        upload_button = tk.Button(root, text="Upload", command=self.upload_image)
        upload_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Referencia para evitar que la imagen sea eliminada por el recolector de basura

    def upload_image(self):
        # Aquí es donde conectarías con el contrato inteligente para subir la imagen
        # Puedes utilizar la biblioteca web3.py para interactuar con contratos Ethereum
        print("Función de carga de imagen. Conéctate con el contrato aquí.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploaderApp(root)
    root.mainloop()

