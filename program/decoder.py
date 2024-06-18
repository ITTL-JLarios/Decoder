from cryptography.fernet import Fernet
from datetime import datetime
import tkinter as tk

class Decoder():
    def __init__(self, root=None, path=None):
        super().__init__()
        self.key = b'3lqUcKreSiI3DzVdHHD7VggudxDIcWCp-bONmioaebE='
        self.fernet = Fernet(self.key)
        self.root = root
        self.path = path


    def decode(self):
        lst = [('Date/Time', 'App', '')]
        with open(self.path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                row = line.split(',')
                time_stamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
                decrypt_app = self.fernet.decrypt(row[1]).decode()
                decrypt_title = self.fernet.decrypt(row[2]).decode()
                lst.append((time_stamp, decrypt_app, decrypt_title))
        
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                entry = tk.Entry(self.root, width=20, fg='blue',
                                    font=('Arial',16,'bold'))
                entry.grid(row=i, column=j)
                entry.insert(tk.END, lst[i][j])
    

    def set_path(self, path:str):
        self.path = path