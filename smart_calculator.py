import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#202124")

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bg="#303134",
    fg="white",
    bd=0
)
display.pack(fill="x", padx=15, pady=20, ipady=15)


def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid Input")


# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#202124")
    frame.pack(expand=True, fill="both", padx=8)

    for item in row:
        if item == "=":
            btn = tk.Button(
                frame,
                text=item,
                font=("Arial", 18, "bold"),
                bg="#34A853",
                fg="white",
                command=calculate
            )
        elif item == "C":
            btn = tk.Button(
                frame,
                text=item,
                font=("Arial", 18, "bold"),
                bg="#EA4335",
                fg="white",
                command=clear
            )
        else:
            btn = tk.Button(
                frame,
                text=item,
                font=("Arial", 18),
                bg="#3C4043",
                fg="white",
                command=lambda x=item: click(x)
            )

        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

root.mainloop()