import tkinter as tk
from tkinter import simpledialog, colorchooser
from tkinterdnd2 import TkinterDnD
from canvas import CanvasEditor
# from toolbar import Toolbar
from toolbar import CanvasEditorApp
from image_handler import DragDropCanvas

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide the main window while dialog is shown
        self.canvas_settings()

    def canvas_settings(self):
        """Dialog box for user input (canvas settings)"""
        dialog = tk.Toplevel()
        dialog.title("Canvas Settings")
        dialog.configure(bg="black")
        dialog.geometry("300x250")
        

        labels = ["Canvas Width:", "Canvas Height:"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(dialog, text=label_text, fg="white", bg="black")
            label.pack(pady=5)
            entry = tk.Entry(dialog)
            entry.pack()
            self.entries.append(entry)

        color_button = tk.Button(dialog, text="Choose Color", command=self.choose_color)
        color_button.pack(pady=5)

        apply_btn = tk.Button(dialog, text="Apply", command=self.apply_settings)
        apply_btn.pack(pady=10)

        self.selected_color = "#ffffff"

    def choose_color(self):
        """Open color picker dialog"""
        color = colorchooser.askcolor()[1]
        if color:
            self.selected_color = color

    def apply_settings(self):
        """Apply settings and open the main editor"""
        width = int(self.entries[0].get())
        height = int(self.entries[1].get())
        color = self.selected_color

        self.root.deiconify()  # Show main window
        self.root.state("zoomed")
        self.root.configure(bg="gray")

        self.canvas = CanvasEditor(self.root, width, height, color)
        # self.toolbar = Toolbar(self.root, self.canvas)
        self.toolbar = CanvasEditorApp(self.root, self.canvas)
        # self.image_handler = DragDropCanvas(self.root, self.canvas)
        self.image_handler = DragDropCanvas(self.root, self.canvas.canvas)


if __name__ == "__main__":
    # root = tk.Tk()
    root = TkinterDnD.Tk()
    app = MainApp(root)
    root.mainloop()
