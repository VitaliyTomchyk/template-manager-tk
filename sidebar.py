import customtkinter as ctk
from window import root
from PIL import Image


#images
os_image = ctk.CTkImage(light_image=Image.open("images/open_sidebar.png"), \
	size=(74, 74))
cs_image = ctk.CTkImage(light_image=Image.open("images/close_sidebar.png"), \
	size=(74, 74))

#sidebar
sidebar = ctk.CTkFrame(root, width=230, height=500, corner_radius=0, \
		fg_color='white')

def open_sidebar():
	sidebar.pack(side='left')
	close_sidebar_btn = ctk.CTkButton(root, text='', image=cs_image, \
	command=lambda: [sidebar.forget(), close_sidebar_btn.forget(), \
	open_sidebar_btn.pack(side='left')], width=0, height=0, fg_color='white')
	close_sidebar_btn.pack(side='left')
	sidebar.pack_propagate(False)
	return

#open sidebar button
open_sidebar_btn = ctk.CTkButton(root, text='', image=os_image, \
		command=lambda: [open_sidebar(), open_sidebar_btn.forget()], \
		width=0, height=0, fg_color='white')
open_sidebar_btn.pack(side='left')
