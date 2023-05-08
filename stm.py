import os
import tkinter as tk
from tkinter import messagebox

from StatusBar import StatusBar
from TipApproach import TipApproach
from DataManipulation import DataManipulation
from Scan import Scan


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Ho_stm remastered")
        
        # fix the size of the window
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # add menubar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # cascade 1
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open...")
        file_menu.add_command(label="Save As...")
        file_menu.add_command(label="Export Multiple...")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # cascade 2
        IO_menu = tk.Menu(menubar, tearoff=0)
        IO_menu.add_command(label="Reinit")
        IO_menu.add_command(label="Elec. Test")
        IO_menu.add_command(label="IO Controls")
        IO_menu.add_command(label="Input...")
        IO_menu.add_command(label="Output...")
        menubar.add_cascade(label="IO", menu=IO_menu)

        # cascade 3
        scanning_menu = tk.Menu(menubar, tearoff=0)
        scanning_menu.add_command(label="Tip Approach...", command=self.create_window_TipApproach)
        scanning_menu.add_command(label="Scan...", command=self.create_window_Scan)
        scanning_menu.add_command(label="Data Manipulation", command=self.create_window_DataManipulation)
        menubar.add_cascade(label="Scanning", menu=scanning_menu)

        # cascade 4
        testbed_menu = tk.Menu(menubar, tearoff=0)
        testbed_menu.add_command(label="Testbed 1")
        testbed_menu.add_command(label="Testbed 2")
        testbed_menu.add_command(label="Testbed 3")
        testbed_menu.add_command(label="Testbed 4")
        testbed_menu.add_command(label="Testbed 5")
        testbed_menu.add_command(label="Testbed 6")
        menubar.add_cascade(label="Testbed", menu=testbed_menu)
        
        # 상태바 생성
        self.status_bar = StatusBar(master=self.master)
        self.status_bar.set("Ready")

        # config 파일에서 is_ready 변수 읽기
        is_ready = self.read_config()

        # 조건 확인 후 경고창 띄우기
        if not is_ready:
            messagebox.showwarning("Warning", "Configuration is not ready!")

    def create_window_TipApproach(self):
        # 새로운 창 생성
        new_window = TipApproach(self.master)

    def create_window_Scan(self):
        # 새로운 창 생성
        new_window = Scan(self.master)
    
    def create_window_DataManipulation(self):
        # 새로운 창 생성
        new_window = DataManipulation(self.master)
    
    def read_config(self):
        # config 파일에서 is_ready 변수 읽기
        config_file = "INITDIR.txt"
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
    app.status_bar.set("Program started")
    app.mainloop()