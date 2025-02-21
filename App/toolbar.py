import tkinter as tk
from tkinter import ttk, font, filedialog, simpledialog
from image_handler import DragDropCanvas

class CanvasEditorApp:
    def __init__(self, root, canvas_editor):
        self.root = root
        # self.root.title("Canvas Editor")

        self.canvas_editor = canvas_editor
        self.image_handler = DragDropCanvas
        
        # Create Notebook (Tab container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=tk.TOP, fill=tk.X)
        
        #! Create Tabs
        self.canvas_tab = ttk.Frame(self.notebook)
        self.image_tab = ttk.Frame(self.notebook)
        self.text_tab = ttk.Frame(self.notebook)
        self.export_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.canvas_tab, text="Canvas")
        self.notebook.add(self.image_tab, text="Image")
        self.notebook.add(self.text_tab, text="Text")
        self.notebook.add(self.export_tab, text="Export")
        
        #! Add Buttons to Tabs
        self.create_canvas_tab()
        self.create_image_tab()
        self.create_text_tab()
        self.create_export_tab()
    

    #? CANVAS TAB
    def create_canvas_tab(self):
        ttk.Button(self.canvas_tab, text="Resize Canvas", command=self.resize_canvas).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Canvas Color").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Canvas Margin").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Border Type").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Border Width").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Border Color").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.canvas_tab, text="Canvas Header").pack(side=tk.LEFT, padx=5, pady=5)
    
    #? IMAGE TAB
    def create_image_tab(self):
         ttk.Button(self.image_tab, text="Crop").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Remove", command=self.remove_selected_image).pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Copy").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Paste").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Duplicate").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Corner Radius").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Border").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Border Color").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Drop Shadow").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Resize").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Rotate").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Move").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Shuffle").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Fit to Screen").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="All Image - Same Size").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Lock/Unlock").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.image_tab, text="Opacity Control").pack(side=tk.LEFT, padx=5, pady=5)    


    #? TEXT TAB
    def create_text_tab(self):
         ttk.Button(self.text_tab, text="Font Size").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Font Color").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Underline").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Bold").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Italic").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Stroke").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Align Left").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Align Center").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Align Right").pack(side=tk.LEFT, padx=5, pady=5)
         ttk.Button(self.text_tab, text="Align Justify").pack(side=tk.LEFT, padx=5, pady=5)
    
    #? EXPORT TAB
    def create_export_tab(self):
        ttk.Button(self.export_tab, text="Save as PDF").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.export_tab, text="Save as SVG").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.export_tab, text="Save as PNG").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.export_tab, text="Save as JPG").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.export_tab, text="Save as JPEG").pack(side=tk.LEFT, padx=5, pady=5)
    
    #todo: RESIZE_CANVAS
    def resize_canvas(self):
        width = simpledialog.askinteger("Resize Canvas", "Enter new width:", minvalue=100, maxvalue=2000)
        height = simpledialog.askinteger("Resize Canvas", "Enter new height:", minvalue=100, maxvalue=2000)
        if width and height:
            self.canvas.config(width=width, height=height)

    #todo: REMOVE_SELECTED_IMAGE
    def remove_selected_image(self):
        self.image_handler.remove_selected_image()
