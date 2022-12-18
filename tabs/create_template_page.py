import customtkinter as ctk 
import tkinter as tk
from window import root


frame = ctk.CTkFrame(root, width=1320, height=1048)

def create_template_page():
	frame.pack(side='right')
	label = ctk.CTkLabel(frame, text='create me jijijiji')
	label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

