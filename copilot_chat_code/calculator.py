import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.input = tk.StringVar()
        self.input.set("0")

        self.label = tk.Label(master, textvariable=self.input, font=("Arial", 20), anchor="e", bg="white", bd=5, relief="sunken")
        self.label.pack(side="top", fill="both", expand=True)

        button_frame = tk.Frame(master)
        button_frame.pack(side="top", padx=5, pady=5)

        self.create_button(button_frame, "7")
        self.create_button(button_frame, "8")
        self.create_button(button_frame, "9")
        self.create_button(button_frame, "/", bg="orange")

        self.create_button(button_frame, "4")
        self.create_button(button_frame, "5")
        self.create_button(button_frame, "6")
        self.create_button(button_frame, "*", bg="orange")

        self.create_button(button_frame, "1")
        self.create_button(button_frame, "2")
        self.create_button(button_frame, "3")
        self.create_button(button_frame, "-", bg="orange")

        self.create_button(button_frame, "0")
        self.create_button(button_frame, ".")
        self.create_button(button_frame, "=", bg="green")
        self.create_button(button_frame, "+", bg="orange")

        self.create_button(button_frame, "C", bg="red")

    def create_button(self, frame, text, bg="white"):
        button = tk.Button(frame, text=text, font=("Arial", 20), bg=bg, bd=2, relief="raised", command=lambda: self.button_click(text))
        button.pack(side="left", padx=5, pady=5, fill="both", expand=True)

    def button_click(self, text):
        if text == "C":
            self.input.set("0")
        elif text == "=":
            try:
                result = str(eval(self.input.get()))
                self.input.set(result)
            except:
                self.input.set("Error")
        else:
            if self.input.get() == "0":
                self.input.set(text)
            else:
                self.input.set(self.input.get() + text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()