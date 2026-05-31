from ansi_codes_test import warn, succ, err
import tkinter as tk

root = tk.Tk(); succ('Root created')
label = tk.Label(root, text='test'); succ('Label created')
label.pack(); succ('Label packed')

root.mainloop(); succ('Root mainloop')

# first time interacting with gui
