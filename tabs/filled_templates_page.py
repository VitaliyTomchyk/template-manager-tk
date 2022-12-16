import customtkinter as ctk 
import tkinter as tk
from window import root


def filled_templates_page():
	lb = ctk.CTkLabel(root, text='I\'m filled')
	lb.place(relx=0.5, rely=0.5, anchor=tk.CENTER)