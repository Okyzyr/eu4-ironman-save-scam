import shutil
import datetime
import os
import tkinter as tk
root = tk.Tk()
path = "C:\\Users\\kcuki\\Documents\\Paradox Interactive\\Europa Universalis IV\\save games\\"
time = datetime.datetime.now()
data = time.strftime("%m.%d-%H.%M.%S")
dir_list = os.listdir(path)

root.title("EU4 Ironman Save Backup")

def backup():
    plik = None
    info = input("Podaj krótkie info do pliku: ")

    for i in range(len(dir_list)):
        if dir_list[i][-3:len(dir_list[i])] == "eu4" and len(dir_list[i]) == 5:
            plik = dir_list[i]

    src_path = path + plik
    dst_path = path + "\\backup\\" + data + " (" + info + ") " + plik
    shutil.copy(src_path, dst_path)
    print('Copied', data)


backup()

root.mainloop()