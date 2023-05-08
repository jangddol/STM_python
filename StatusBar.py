import tkinter as tk

class StatusBar:
    def __init__(self, master=None):
        self.master = master
        
        # 상태바 생성
        self.status_bar = tk.Label(self.master, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def set(self, text):
        self.status_bar.config(text=text)
        self.status_bar.update_idletasks()