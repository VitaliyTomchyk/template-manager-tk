import customtkinter as ctk 
import tkinter as tk
from window import root


frame = ctk.CTkFrame(root, width=1750, height=1080, border_width=1.5)
textbox = ctk.CTkTextbox(frame, width=1000, height=706, border_width=1.5, \
		font=("Roboto", 18), undo=True)
save_btn = ctk.CTkButton(frame, width=150, height=60, text="Next step", \
		font=("Roboto", 15), command=lambda:[save_ct_text()])
working_file = None

def create_template_page():
	frame.pack(side='right')
	textbox.place(relx=0.40, rely=0.5, anchor=tk.CENTER)
	save_btn.place(relx=0.892, rely=0.9, anchor=tk.CENTER)

	global working_file
	if working_file == None:
		text_file = open('templates/ct_working_template.txt', 'a')
		working_file= 'templates/ct_working_template.txt'
	else:
		text_file = open('templates/ct_working_template.txt', 'r')
		text = text_file.read()
		textbox.insert(1.0, text)

#save working file when changing tabs
def save_ct_text():
	with open('templates/ct_working_template.txt', "w") as file:
		file.write(textbox.get("0.0", "end"))
		file.close()