import tkinter as tk

class DataManipulation(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Data Manipulation")
        
        self.geometry("300x200")
        
        # 버튼 생성
        self.new_button = tk.Button(self, text="Click me", command=self.new_button_clicked)
        self.new_button.grid(row=0, column=0, padx=10, pady=10)
        self.new_button.pack()
        
    def new_button_clicked(self):
        print("New button clicked!")