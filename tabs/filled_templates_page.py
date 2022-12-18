import customtkinter as ctk 
import tkinter as tk
from window import root


frame = ctk.CTkFrame(root, width=1320, height=1048)

def filled_templates_page():
	frame.pack(side='right')
	label = ctk.CTkLabel(frame, text="I'm filled")
	label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
