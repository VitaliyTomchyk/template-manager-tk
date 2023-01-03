import customtkinter as ctk
from window import root
from tabs.create_template_page import create_template_page, save_ct_text, \
                                      ct_window_alert, frame as frame1
from tabs.edit_template_page import edit_template_page, frame as frame2
from tabs.fill_template_page import fill_template_page, frame as frame3
from tabs.filled_templates_page import filled_templates_page, frame as frame4
from tabs.settings_page import settings_page, frame as frame5


# sidebar
sidebar = ctk.CTkFrame(root, width=230, height=504, corner_radius=10)


# buttons in sidebar
create_template_btn = ctk.CTkButton(sidebar)
edit_template_btn = ctk.CTkButton(sidebar)
fill_template_btn = ctk.CTkButton(sidebar)
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
    frame1.forget(), frame2.forget(), frame3.forget(), frame4.forget(),
    frame5.forget()


lp = fill_template_page


def goto(page):
    global lp
    lp = page
    page_refresh()
    if page == create_template_page:
        return create_template_page()
    if page == edit_template_page:
        return edit_template_page()
    if page == fill_template_page:
        return fill_template_page()
    if page == filled_templates_page:
        return filled_templates_page()
    else:
        return settings_page()


# each button parameters
create_template_btn = button_parameters(create_template_btn, 'Create template',
                                        create_template_page, 14)
edit_template_btn = button_parameters(edit_template_btn, 'Edit template',
                                      edit_template_page, 112)
fill_template_btn = button_parameters(fill_template_btn, 'Fill template',
                                      fill_template_page, 210)
filled_templates_btn = button_parameters(filled_templates_btn,
                                         'Filled templates',
                                         filled_templates_page, 308)
settings_btn = button_parameters(settings_btn, 'Settings', settings_page, 406)


def active_button(button):
    button.configure(fg_color='#36719F')
    return


def unactive_buttons():
    create_template_btn.configure(fg_color='#3B8ED0')
    edit_template_btn.configure(fg_color='#3B8ED0')
    filled_templates_btn.configure(fg_color='#3B8ED0')
    fill_template_btn.configure(fg_color='#3B8ED0')
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
