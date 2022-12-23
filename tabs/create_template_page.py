import customtkinter as ctk
import tkinter as tk
from window import root
from tkinter import messagebox


frame = ctk.CTkFrame(root, width=1750, height=1080, border_width=1.5,
                     fg_color="#3B8ED0")
sframe = ctk.CTkFrame(frame, width=1200, height=710, border_width=0,
                      fg_color="#3B8ED0")
textbox = ctk.CTkTextbox(sframe, width=894, height=710, font=("Roboto", 18),
                         undo=True)
tframe = ctk.CTkFrame(sframe, width=300, height=665, corner_radius=6)
fframe = ctk.CTkFrame(sframe, width=300, height=40, corner_radius=6)
refresh = ctk.CTkButton(fframe, width=120, height=20, text="Refresh",
                        font=("Roboto", 15), command=lambda: [save_ct_text()])
save = ctk.CTkButton(fframe, width=120, height=20, text="Save",
                     font=("Roboto", 15), command=lambda: [save_ct_text()])
working_file = None


def create_template_page():
    frame.pack(side='right')
    sframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    textbox.place(relx=0, rely=0.5, anchor=tk.W)
    tframe.place(relx=1.0, rely=0.4675, anchor=tk.E)
    fframe.place(relx=1.0, rely=0.972, anchor=tk.E)
    refresh.place(relx=0.2725, rely=0.5, anchor=tk.CENTER)
    save.place(relx=0.7275, rely=0.5, anchor=tk.CENTER)

    global working_file
    if working_file is None:
        text_file = open('templates/ct_working_template.txt', "a")
        working_file = 'templates/ct_working_template.txt'
    else:
        text_file = open('templates/ct_working_template.txt', "r")
        text = text_file.read()
        textbox.insert(1.0, text)


# save working file when changing tabs
def save_ct_text():
    with open("templates/ct_working_template.txt", "w") as f:
        f.write(textbox.get("0.0", "1.0"))
        f.close()


# save template as
def save_template(name):
    bar_name = name.replace(" ", "_")
    with open(f"templates/blank_templates/{bar_name}.txt", "a") as f:
        f.write(str(textbox.get("1.0", "end")))
        f.close()


# save created template window
def swindow():
    global window
    window = ctk.CTkToplevel(root)
    window.title("Save your created temlplate")
    window.geometry("400x120")
    window.resizable(False, False)
    window.transient(root)
    window.grab_set()

    text = ctk.CTkLabel(window, text_color="#3B8ED0", font=("Roboto", 17),
                        text="Save template as:")
    entry = ctk.CTkEntry(window, width=350, height=35,
                         placeholder_text="Enter the name of template here",
                         font=("Roboto", 15))
    button = ctk.CTkButton(window, text="Save and exit", fg_color="white",
                           width=200, height=30, text_color="#3B8ED0",
                           command=lambda: [save_template(entry.get()),
                                            root.destroy()])

    text.place(x=20, y=10)
    entry.place(x=20, y=40)
    button.place(x=100, y=85)


# message box for saving files
def window_questions(response):
    if response is False:
        root.destroy()
    if response is True:
        try:
            window.destroy()
        except NameError:
            pass
        finally:
            swindow()


def not_saved_ct():
    if working_file is None:
        root.destroy()
    else:
        response = messagebox.askyesnocancel("Quit",
                                             "Would you like to save your \
                                              created template?")
        window_questions(response)
