import tkinter as tk
from tkinter.filedialog import askopenfilename

from program.decoder import Decoder

root = tk.Tk()
decoder = Decoder(root=root)

# Program title and TK Variables
root.title('Decoder')
my_path = tk.Variable()
y_scroll = tk.Scrollbar(root, orient='vertical').grid(column=3)

def find_file():
    file_name = askopenfilename()
    decoder.set_path(file_name)
    my_path.set(file_name)

def main():
    widget = tk.Label(root, text='TTL Decoder').grid(row=0)
    label = tk.Label(root, text='File Path').grid(row=2, column=0)
    browser_button = tk.Button(root, text='Browser File',
                               width=25, command=find_file).grid(row=2, column=2)
    path = tk.Entry(root, textvariable=my_path).grid(row=2, column=1)

    decode_button = tk.Button(root, text='Decode',
                                command=decoder.decode).grid(row=3, column=2)

    root.mainloop()

main()