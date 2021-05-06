import os
import tkinter as tk
import subprocess

"""Author
https://github.com/free2fork/
https://free2fork.dev
"""

root= tk.Tk()
root.title('Pop-up PIP')


canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Hit the buttons!', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 16))
canvas1.create_window(150, 80, window=label1)

"""After clicking the button a Prompt window should pop-up.
Don't panic :)
"""
def upgradePIP ():
    os.system('start cmd /k python -m pip install --user --upgrade pip')
 
button1 = tk.Button(text='      Upgrade PIP     ', command=upgradePIP, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button1)


"""After clicking the button a PowerShell window should pop-up.
Make sure you have Powershell installed.
Or change the command inside subprocessl.call() to use Prompt.
"""
def upgdatePkgs ():
    completed = subprocess.call(["powershell.exe", "pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}"])
    
button2 = tk.Button(text='      Update Packages     ', command=upgdatePkgs, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 220, window=button2)

root.mainloop()
