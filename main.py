import os
import ctypes
import tkinter as tk
from tkinter import filedialog

SPI_SETDESKWALLPAPER = 20

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

class WallpaperChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wallpaper Changer")

        self.image_path = tk.StringVar()

        # Create Widgets
        self.label = tk.Label(root, text="Select Wallpaper:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.image_path, width=40)
        self.entry.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_button.pack(pady=10)

        self.change_button = tk.Button(root, text="Set Wallpaper", command=self.set_wallpaper)
        self.change_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        self.image_path.set(file_path)

    def set_wallpaper(self):
        image_path = self.image_path.get()
        if os.path.isfile(image_path):
            set_wallpaper(image_path)
            tk.messagebox.showinfo("Success", "Wallpaper changed successfully!")
        else:
            tk.messagebox.showerror("Error", "Invalid file or path. Please choose a valid image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WallpaperChangerApp(root)
    root.mainloop()
