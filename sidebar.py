import customtkinter as ctk
import tkinter as tk
from window import root
from tabs.create_template_page import create_template_page
from tabs.edit_template_page import edit_template_page
from tabs.fill_template_page import fill_template_page
from tabs.filled_templates_page import filled_templates_page
from tabs.settings_page import settings_page


#sidebar
sidebar = ctk.CTkFrame(root, width=230, height=504, corner_radius=10)

#buttons in sidebar
create_template_btn = ctk.CTkButton(sidebar)
edit_template_btn = ctk.CTkButton(sidebar)
fill_template_btn = ctk.CTkButton(sidebar)
filled_templates_btn = ctk.CTkButton(sidebar)
settings_btn = ctk.CTkButton(sidebar)

#button parameters
def button_parameters(button, name, page, ix, iy):
	button = ctk.CTkButton(sidebar, text=name, \
	width=150, height=84, corner_radius=12, font=ctk.CTkFont(size=17), \
	command=lambda: [unactive_buttons(), active_button(button), \
	goto(page)])
	button.place(x=ix, y=iy)
	return button

#each button parameters
create_template_btn =button_parameters(create_template_btn, 'Create template', \
    1, 38, 14)
edit_template_btn =button_parameters(edit_template_btn, 'Edit template', \
	2, 38, 112)
fill_template_btn =button_parameters(fill_template_btn, 'Fill template', \
	3, 38, 210)
filled_templates_btn =button_parameters(filled_templates_btn, \
	'Filled templates', 4, 38, 308)
settings_btn =button_parameters(settings_btn, 'Settings', 5, 38, 406)


def goto(page):
	if page == 1:
		return create_template_page()
	if page == 2:
		return edit_template_page()
	if page == 3:
		return fill_template_page()
	if page == 4:
		return filled_templates_page()
	else:
		return settings_page()

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
