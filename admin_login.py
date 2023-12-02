import os
import customtkinter
from tkinter import messagebox
import sqlite3

def login():
    pass

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.title("Login as admin")
root.geometry("500x400+550+250")


fram=customtkinter.CTkFrame(root)
fram.pack(fill="both", expand=True,padx=60, pady=20)

labl=customtkinter.CTkLabel(fram, text="Login as admin", font=("Arial", 20,'bold'))
labl.pack(padx=10, pady=10)
entr1=customtkinter.CTkEntry(fram,placeholder_text='Username')
entr1.pack(padx=10, pady=10)

entr2=customtkinter.CTkEntry(fram,placeholder_text='Password', show="*")
entr2.pack(padx=10, pady=12)

checkbox=customtkinter.CTkCheckBox(fram, text="Remember me")
checkbox.pack(padx=10, pady=10)

butt=customtkinter.CTkButton(fram, text="Login", command=login)
butt.pack(padx=10, pady=12)

root.mainloop()