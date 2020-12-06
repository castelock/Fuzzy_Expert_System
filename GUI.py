import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self, window_name):
        super().__init__()
        self.window_name = window_name
        self.title(window_name)
        self.label_text = tk.StringVar()
        self.label_text.set("My first Window")

        self.label = tk.Label(self, textvariable=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        goodbye_button = tk.Button(self, text="Exit", command=self.goodbye)
        goodbye_button.pack(side=tk.BOTTOM, expand=1, padx=100, pady=50)

    def goodbye(self):
        self.label_text.set("Goodbye!!!")
        msgbox.showinfo("Quit", "See you soon!!!")
        self.after(1000, self.destroy)

    def exit(self):
        self.after(0, self.destroy)