import customtkinter as ctk 
import tkinter as tk
from window import root


def settings_page():
	lb = ctk.CTkLabel(root, text='configure me')
	lb.place(relx=0.5, rely=0.5, anchor=tk.CENTER)