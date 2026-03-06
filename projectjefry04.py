import tkinter as tk

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")
root.resizable(False, False)

# Variabel untuk input
expression = ""

# Fungsi untuk menambahkan angka/operator
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

# Fungsi untuk menghitung hasil
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Fungsi untuk menghapus semua
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar untuk display
equation = tk.StringVar()

# Entry display
entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=10, relief="sunken", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Frame tombol
frame = tk.Frame(root)
frame.pack()

# Tombol-tombol
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2)
]

for (text,row,col) in buttons:
    tk.Button(frame, text=text, width=5, height=2,
              font=("Arial",14),
              command=lambda t=text: press(t)).grid(row=row, column=col)

# Tombol =
tk.Button(frame, text='=', width=5, height=2,
          font=("Arial",14),
          bg="lightgreen",
          command=equalpress).grid(row=4, column=3)

# Tombol Clear
tk.Button(root, text='Hapus', height=2,
          font=("Arial",12),
          bg="tomato",
          command=clear).pack(fill="both", padx=10, pady=5)

root.mainloop()