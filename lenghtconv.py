import tkinter as tk

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x400")
root.configure(bg="#000000")

def convert_to_cm():
    cm = float(entry.get()) * 2.54
    result_label.config(text=str(cm) + " cm")

instruction_label = tk.Label(root, text="Enter Length in Inches:", font=("Algerian", 22, "bold italic"), fg="black")
instruction_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), width=10)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", font=("Comic Sans MS", 16, "bold italic"), width=20, height=2, bg="#ffff00", fg="black", command=convert_to_cm)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Comic Sans MS", 16, "bold"))
result_label.pack(pady=20)

root.mainloop()
