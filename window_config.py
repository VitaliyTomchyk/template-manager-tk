import customtkinter as ctk
from window import root
from tabs.editing_mode import editing_mode, save_ct_text, \
                                      ct_window_alert, frame as frame1
from tabs.blank_templates_page import blank_templates_page, frame as frame2
from tabs.filled_templates_page import filled_templates_page, frame as frame3
from tabs.settings_page import settings_page, frame as frame4


# sidebar
sidebar = ctk.CTkFrame(root, width=230, height=406, corner_radius=10)


# buttons in sidebar
working_page_btn = ctk.CTkButton(sidebar)
blank_templates_btn = ctk.CTkButton(sidebar)
filled_templates_btn = ctk.CTkButton(sidebar)
settings_btn = ctk.CTkButton(sidebar)


# save text files when changing tabs
def save_text():
    save_ct_text()


# button parameters
def button_parameters(button, name, page, y_pos):
    button = ctk.CTkButton(sidebar, text=name, width=150, height=84,
                           corner_radius=12, font=ctk.CTkFont(size=17),
                           command=lambda: [save_text(), unactive_buttons(),
                                            active_button(button), goto(page)])
    button.place(x=38, y=y_pos)
    return button


# refresh pages
def page_refresh():
    frame1.forget(), frame2.forget(), frame3.forget(), frame4.forget()


lp = blank_templates_page


def goto(page):
    global lp
    lp = page
    page_refresh()
    if page == editing_mode:
        return editing_mode()
    if page == blank_templates_page:
        return blank_templates_page()
    if page == filled_templates_page:
        return filled_templates_page()
    else:
        return settings_page()


# each button parameters
working_page_btn = button_parameters(working_page_btn, 'Working file',
                                     editing_mode, 14)
blank_templates_btn = button_parameters(blank_templates_btn, 'Blank templates',
                                        blank_templates_page, 112)
filled_templates_btn = button_parameters(filled_templates_btn,
                                         'Filled templates',
                                         filled_templates_page, 210)
settings_btn = button_parameters(settings_btn, 'Settings', settings_page, 308)


def active_button(button):
    button.configure(fg_color='#36719F')


def active_blank_tp():
    blank_templates_btn.configure(fg_color='#36719F')


def unactive_buttons():
    working_page_btn.configure(fg_color='#3B8ED0')
    blank_templates_btn.configure(fg_color='#3B8ED0')
    filled_templates_btn.configure(fg_color='#3B8ED0')
    settings_btn.configure(fg_color='#3B8ED0')


def open_sidebar():
    sidebar.pack(side='left')
    close_sidebar_btn = ctk.CTkButton(root, text='<',
                                      command=lambda: [save_text(),
                                                       sidebar.forget(),
                                                       close_sidebar_btn.
                                                       forget(),
                                                       open_sidebar_btn.
                                                       pack(side='left'),
                                                       goto(lp)],
                                      width=30, height=82,
                                      corner_radius=0, fg_color='gray86',
                                      font=ctk.CTkFont(size=30),
                                      text_color='#3B8ED0')
    close_sidebar_btn.pack(side='left')
    sidebar.pack_propagate(True)
    return


# open sidebar button
open_sidebar_btn = ctk.CTkButton(root, text='>', command=lambda: [save_text(),
                                 open_sidebar(),
                                 open_sidebar_btn.forget(), goto(lp)],
                                 width=30, height=82, corner_radius=0,
                                 fg_color='grey86', font=ctk.CTkFont(size=30),
                                 text_color='#3B8ED0')
open_sidebar_btn.pack(side='left')


# message box
def not_saved_question():
    ct_window_alert()


root.protocol("WM_DELETE_WINDOW", not_saved_question)
