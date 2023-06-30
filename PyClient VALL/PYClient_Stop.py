from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os

def button1_clicked():
    os.system("taskkill /f /im KillAura.exe")


def button2_clicked():
        os.system("taskkill /f /im AimBot.exe")


def button3_clicked():
        os.system("taskkill /f /im openproject.exe")


def button4_clicked():
        os.system("taskkill /f /im Tp+.exe")


def keyclick():
        os.system("taskkill /f /im key.exe")


def run():
        os.system("taskkill /f /im PyClient_V4.exe")


window = tk.Tk()
window.title("PYClient_Stop(Version Launcher)")
window.geometry("400x200")
window.configure(bg="black")

button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=30)

button1 = tk.Button(button_frame, text="停\n止\n杀\n戮\n光\n环", command=button1_clicked, bg="white", fg="black",
                        bd=2, relief="solid", width=5, height=6)
button1.grid(row=0, column=0, padx=10)

button2 = tk.Button(button_frame, text="停\n止\n自\n动\n瞄\n准", command=button2_clicked, bg="white", fg="black",
                        bd=2, relief="solid", width=5, height=6)
button2.grid(row=0, column=1, padx=10)

button3 = tk.Button(button_frame, text="停\n止\n自\n动\n连\n点", command=button3_clicked, bg="white", fg="black",
                        bd=2, relief="solid", width=5, height=6)
button3.grid(row=0, column=2, padx=10)

button4 = tk.Button(button_frame, text="停\n止\n瞬\n移", command=button4_clicked, bg="white", fg="black", bd=2,
                        relief="solid", width=5, height=6)
button4.grid(row=0, column=3, padx=10)

run = tk.Button(button_frame, text="停\n止\n运\n行\n检\n查", command=run, bg="white", fg="black", bd=2,
                    relief="solid", width=5, height=6)
run.grid(row=0, column=4, padx=10)

run = tk.Button(button_frame, text="停\n止\n键\n盘\n连\n点", command=keyclick, bg="white", fg="black", bd=2,
                    relief="solid", width=5, height=6)
run.grid(row=0, column=5, padx=10)

window.mainloop()

