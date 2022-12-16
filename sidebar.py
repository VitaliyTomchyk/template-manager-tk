import customtkinter as ctk
from window import root
from PIL import Image


#images
#os_image = ctk.CTkImage(light_image=Image.open("images/open_sidebar.png"), \
#	size=(74, 74))
#cs_image = ctk.CTkImage(light_image=Image.open("images/close_sidebar.png"), \
#	size=(74, 74))

#sidebar
sidebar = ctk.CTkFrame(root, width=230, height=500, corner_radius=0)

def open_sidebar():
	sidebar.pack(side='left')
	close_sidebar_btn = ctk.CTkButton(root, text='<', \
	command=lambda: [sidebar.forget(), close_sidebar_btn.forget(), \
	open_sidebar_btn.pack(side='left')], width=30, height=82, \
	corner_radius=3, fg_color='gray86', font=ctk.CTkFont(size=30), \
	text_color='#3B8ED0')
	close_sidebar_btn.pack(side='left')
	sidebar.pack_propagate(False)
	return

#open sidebar button
open_sidebar_btn = ctk.CTkButton(root, text='>', \
		command=lambda: [open_sidebar(), open_sidebar_btn.forget()], \
		width=30, height=82, corner_radius=3, fg_color='grey86', \
		font=ctk.CTkFont(size=30), text_color='#3B8ED0')
open_sidebar_btn.pack(side='left')
