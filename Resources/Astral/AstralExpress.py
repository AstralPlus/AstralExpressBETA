from customtkinter import *
import tkinter as tk
import subprocess
import os
import shutil
from tkinter import filedialog
from tkinter import Tk

current_dir = os.path.dirname(os.path.abspath(__file__))
app = CTk()
app.geometry("355x255")
app.resizable(True, False)

app.wm_iconbitmap(os.path.join(current_dir, 'astral.ico'))
app.wm_title("Astral Express for Star Rail 2.2 Beta")
set_default_color_theme("blue")

tabview = CTkTabview(master=app)
tabview.pack(padx=0, pady=0)
tabview.add("Server")

def start():
    gameserver_exe = os.path.join(current_dir, "../RobinSR/gameserver/gameserver.exe")
    sdkserver_exe = os.path.join(current_dir, "../RobinSR/sdkserver/sdkserver.exe")
    subprocess.Popen(["start", gameserver_exe], shell=True)
    subprocess.Popen(["start", sdkserver_exe], shell=True)

def patch():
    try:        
        dll_src = os.path.join(current_dir, "../GamePatch/mhypbase.dll")
        bytes_src = os.path.join(current_dir, "../GamePatch/28d4618f056f0865279208b5b269d323.bytes")
        
        root = Tk()
        root.withdraw()
        dest_dir = filedialog.askdirectory()
        
        dll_dest = os.path.join(dest_dir, "mhypbase.dll")
        bytes_dest = os.path.join(dest_dir, "StarRail_Data/StreamingAssets/DesignData/Windows/28d4618f056f0865279208b5b269d323.bytes")
        
        shutil.move(dll_src, dll_dest)
        shutil.move(bytes_src, bytes_dest)
        
        button2.pack_forget()
        
        print("Game patched successfully.")
    except Exception as e:
        print(f"An error occurred while patching the game: {e}")


def exit():
    app.destroy()


button1 = CTkButton(master=tabview.tab("Server"), text="Start server", command=start, fg_color="#C6829B", hover_color="#843E58")
button2 = CTkButton(master=tabview.tab("Server"), text="Patch game", command=patch, fg_color="#668cbd", hover_color="#37506F")
button3 = CTkButton(master=tabview.tab("Server"), text="Exit", command=exit, fg_color="#A60003", hover_color="dark red")
button1.pack(padx=10, pady=10)
button2.pack(padx=10, pady=10)
button3.pack(padx=10, pady=10)

app.mainloop()