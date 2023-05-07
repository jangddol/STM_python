import os
import tkinter as tk
from tkinter import messagebox

class NewWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("New Window")
        
        self.geometry("300x200")
        
        # 버튼 생성
        self.new_button = tk.Button(self, text="Click me", command=self.new_button_clicked)
        self.new_button.grid(row=0, column=0, padx=10, pady=10)
        self.new_button.pack()
        
    def new_button_clicked(self):
        print("New button clicked!")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Ho_stm remastered")
        
        # config 파일에서 is_ready 변수 읽기
        is_ready = self.read_config()
        
        # 조건 확인 후 경고창 띄우기
        if not is_ready:
            messagebox.showwarning("Warning", "Configuration is not ready!")
            return
        
        # add menubar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # add menu "File"
        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # add menu item "New Window"
        file_menu.add_command(label="New Window", command=self.create_new_window)
        
    def create_new_window(self):
        # 새로운 창 생성
        new_window = NewWindow(self.master)
        new_window.title("New Window")
        
    def read_config(self):
        # config 파일에서 is_ready 변수 읽기
        config_file = "config.txt"
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                config_data = f.read()
                is_ready = config_data.strip().lower() == "true"
                return is_ready
        else:
            return False
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()