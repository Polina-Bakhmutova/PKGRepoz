import tkinter as tk
from tkinter import ttk
from colorspacious import cspace_converter

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")

        self.rgb_label = tk.Label(root, text="RGB:")
        self.rgb_label.grid(row=0, column=0, padx=5, pady=5)
        self.rgb_var = tk.StringVar(value="255, 0, 0")
        self.rgb_entry = tk.Entry(root, textvariable=self.rgb_var)
        self.rgb_entry.grid(row=0, column=1, padx=5, pady=5)

        self.hsv_label = tk.Label(root, text="HSV:")
        self.hsv_label.grid(row=1, column=0, padx=5, pady=5)
        self.hsv_var = tk.StringVar(value="0, 100, 100")
        self.hsv_entry = tk.Entry(root, textvariable=self.hsv_var)
        self.hsv_entry.grid(row=1, column=1, padx=5, pady=5)

        self.lab_label = tk.Label(root, text="LAB:")
        self.lab_label.grid(row=2, column=0, padx=5, pady=5)
        self.lab_var = tk.StringVar(value="50, 0, 0")
        self.lab_entry = tk.Entry(root, textvariable=self.lab_var)
        self.lab_entry.grid(row=2, column=1, padx=5, pady=5)

        self.color_frame = tk.Frame(root, width=50, height=50, bg=self.get_rgb_color())
        self.color_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.update_button = ttk.Button(root, text="Update", command=self.update_color)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=10)

    def get_rgb_color(self):
        rgb_values = [int(x) for x in self.rgb_var.get().split(',')]
        return "#{:02x}{:02x}{:02x}".format(*rgb_values)

    def update_color(self):
        try:
            # Convert RGB to HSV and LAB
            rgb_values = [int(x) for x in self.rgb_var.get().split(',')]
            hsv_result = cspace_converter("sRGB1", "CAM02-UCS")(rgb_values)
            lab_result = cspace_converter("sRGB1", "CIELab")(rgb_values)

            # Display the converted values
            self.hsv_var.set(", ".join(map(str, map(round, hsv_result))))
            self.lab_var.set(", ".join(map(str, map(round, lab_result))))

            # Update the color frame
            self.color_frame.config(bg=self.get_rgb_color())
        except ValueError:
            print("Invalid input. Please enter comma-separated integer values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
