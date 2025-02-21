import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinterdnd2 import TkinterDnD, DND_FILES

class DragDropCanvas:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.images = {}
        self.image_sizes = {}
        self.selected = None
        self.border_id = None

        # Enable Drag & Drop
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind("<<Drop>>", self.on_drop)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    #! drop image
    def on_drop(self, event):
        """Handle files drop (single, multiple, or folder)"""
        files = self.root.tk.splitlist(event.data)
        image_paths = []

        for file in files:
            if os.path.isdir(file):
                image_paths.extend(self.get_image_from_folder(file))
            else:
                image_paths.append(file)

        self.add_images(image_paths)

    #! get_image_from_folder
    def get_image_from_folder(self, folder_path):
        """Fetch all images from a given folder"""
        valid_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp"}
        return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(tuple(valid_extensions))]

    #! add image
    def add_images(self, image_paths):
        for path in image_paths:
            try:
                image = Image.open(path)
                # image.thumbnail((200, 200))
                img_tk = ImageTk.PhotoImage(image)

                # NEW : Store actual image size
                width, height = image.size
                self.image_sizes[path] = (width, height)

                # place image on canvas
                img_id = self.canvas.create_image(100, 100, image=img_tk, anchor="center")

                # Keep reference to prevent garbage collection
                self.images[img_id] = (img_tk, path) 
               
                # Bind actions to the image
                self.canvas.tag_bind(img_id, "<Button-1>", self.select_image)
                self.canvas.tag_bind(img_id, "<B1-Motion>", self.move_image)

            except Exception as e:
                print(f"Error loading image {path}:{e}")

    #! load the image
    def load_image(self, file_path):
        try:
            image = Image.open(file_path)  # ✅ Ensure `file_path` is a valid string
            image = image.resize((200, 200))  # Resize if needed
            self.tk_image = ImageTk.PhotoImage(image)  
            self.canvas.create_image(100, 100, image=self.tk_image, anchor="center")
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")  # Debugging print

    #! Select the image
    def select_image(self, event):
        """Select an image (apply border)."""
        closest = self.canvas.find_closest(event.x, event.y)  # Get nearest image
        if not closest:
            return
        img_id = closest[0]

        # if clicking on already selected images -> deselect
        if self.selected == img_id:
            self.deselect_image()
            return

        # Remove previous selection
        self.deselect_image()

        # select new image
        self.selected = img_id
        x, y = self.canvas.coords(img_id)

        # NEW: Retrieve the actual image size dynamically
        _, img_path = self.images[img_id]
        width, height = self.image_sizes[img_path] 

        # Adjust border to match image size
        self.border_id = self.canvas.create_rectangle(x - width // 2, y - height // 2, x + width // 2, y + height // 2, outline="gray", width=2, tags="border")

        # Enable Delete button
        # self.delete_button.config(state=tk.NORMAL)

    #! get_selected_image
    def get_selected_image(self):
        return self.selected

    #! deselect_image
    def deselect_image(self):
        """Deselect selected image"""
        if self.border_id:
            self.canvas.delete(self.border_id)  # Remove border
            self.border_id = None
        self.selected = None

    #! remove_selected_image
    def remove_selected_image(self):
        """Remove the selected image from the canvas."""
        if self.selected:
            self.canvas.delete(self.selected)
            if self.border_id:
                self.canvas.delete(self.border_id)
                self.border_id = None
            del self.images[self.selected]
            self.selected = None

    #! move_image
    def move_image(self, event):
        """Move selected image"""
        if self.selected:
            self.canvas.coords(self.selected, event.x, event.y)

            # Move border if exists
            if self.border_id:
                _, img_path = self.images[self.selected]
                width, height = self.image_sizes[img_path] # Get stored size
                self.canvas.coords(self.border_id, event.x - width // 2, event.y - height // 2, event.x + width // 2 , event.y + height // 2)

    #! on_canvas_click
    def on_canvas_click(self, event):
        """Deselect all images when clicking empty canvas"""
        clicked_item = self.canvas.find_closest(event.x, event.y)
        # if not self.canvas.find_closest(event.x, event.y):
            # self.deselect_image()
        if not clicked_item:
            self.deselect_image()

    #! Delete images
    def delete_selected_images(self):
        """Delete selected images from the canvas"""
        if self.selected:
            self.canvas.delete(self.selected)  # Remove from canvas
            if self.border_id:
                self.canvas.delete(self.border_id)  # Remove border
                self.border_id = None
                
            _, img_path = self.images[self.selected]    
            del self.images[self.selected]  # Remove from stored images
            del self.image_size[img_path] # Remove size reference 
            self.selected = None

