import customtkinter as ctk 
import tkinter as tk
from window import root


def fill_template_page():
	lb = ctk.CTkLabel(root, text='fill me')
	lb.place(relx=0.5, rely=0.5, anchor=tk.CENTER)