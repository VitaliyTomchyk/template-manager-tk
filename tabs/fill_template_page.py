import customtkinter as ctk 
import tkinter as tk
from window import root


frame = ctk.CTkFrame(root, width=1280, height=720)

def fill_template_page():
	frame.pack(side='right')
	label = ctk.CTkLabel(frame, text='fill me')
	label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
