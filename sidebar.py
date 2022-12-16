import customtkinter as ctk
import tkinter as tk
from window import root
from tabs.create_template_page import create_template_page


#sidebar
sidebar = ctk.CTkFrame(root, width=230, height=504, corner_radius=10)

#buttons in sidebar
create_template_btn = ctk.CTkButton(sidebar, text='Create template', \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(create_template_btn), \
	create_template_page()])
edit_template_btn = ctk.CTkButton(sidebar, text='Edit template', \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(edit_template_btn)])
fill_template_btn = ctk.CTkButton(sidebar, text='Fill template', \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(fill_template_btn)])
filled_templates_btn = ctk.CTkButton(sidebar, text='Filled templates', \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(filled_templates_btn)])
settings_btn = ctk.CTkButton(sidebar,text='Settings', \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(settings_btn)])


#button placements
create_template_btn.place(x=38, y=14)
edit_template_btn.place(x=38, y=112)
fill_template_btn.place(x=38, y=210)
filled_templates_btn.place(x=38, y=308)
settings_btn.place(x=38,y=406)

def active_button(button):
	button.configure(fg_color='#36719F')

def unactive_buttons():
	create_template_btn.configure(fg_color='#3B8ED0')
	edit_template_btn.configure(fg_color='#3B8ED0')
	filled_templates_btn.configure(fg_color='#3B8ED0')
	fill_template_btn.configure(fg_color='#3B8ED0')
	settings_btn.configure(fg_color='#3B8ED0')

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
