import tkinter as tk

class CanvasEditor:
    def __init__(self, root, width, height, bg_color):
        self.canvas = tk.Canvas(root, width=width, height=height, bg=bg_color, relief="ridge", bd=2)
        self.canvas.place(relx=0.5, rely=0.55, anchor="center")

    def resize_canvas(self, width, height, color):
        """Resize and recolor canvas"""
        self.canvas.config(width=width, height=height, bg=color)
