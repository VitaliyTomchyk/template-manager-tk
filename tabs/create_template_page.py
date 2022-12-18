import customtkinter as ctk 
import tkinter as tk
from window import root


frame = ctk.CTkFrame(root, width=1750, height=1080, border_width=1.5)

def create_template_page():
	frame.pack(side='right')

	textbox = ctk.CTkTextbox(frame, width=1000, height=706, border_width=1.5, \
		font=("Roboto", 18))
	textbox.place(relx=0.40, rely=0.5, anchor=tk.CENTER)

	save_btn = ctk.CTkButton(frame, width=150, height=60, text="Next step", \
		font=("Roboto", 15))
	save_btn.place(relx=0.892, rely=0.9, anchor=tk.CENTER)
