import tkinter as tk

def converter():
    inch = float(entry_inch.get())
    cm = inch * 2.54
    label_result.config(text=f"{cm:.2f} cm")

root = tk.Tk()
root.title("Inch to Centimeter Converter")
root.geometry("300x150")

label_prompt = tk.Label(root, text="Enter value in inches:")
label_prompt.pack(pady=5)

entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=converter)
button_convert.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

root.mainloop()