import customtkinter as ctk
import tkinter as tk
import window_config as wc
from tabs.blank_templates_page import blank_templates_page
from window import root
from tkinter import messagebox
from PIL import Image
import re
import json
import os


# images
img_save = ctk.CTkImage(Image.open("images/icons-save.png"), size=(30, 30))
img_refresh = ctk.CTkImage(Image.open("images/icons-update-left-rotation.png"),
                           size=(30, 30))
img_close = ctk.CTkImage(Image.open("images/icons-close.png"),
                         size=(30, 30))
img_plus = ctk.CTkImage(Image.open("images/icons-plus.png"),
                        size=(30, 30))


# variables highliter
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, regexp=False):
        start = self.index("1.0")
        end = self.index("end")
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit",
                                count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")


frame = ctk.CTkFrame(root, width=1750, height=1080, border_width=1.5,
                     fg_color="#3B8ED0")
sframe = ctk.CTkFrame(frame, width=1200, height=710, border_width=0,
                      fg_color="#3B8ED0")
textbox = CustomText(sframe, font=("Roboto", 15), width=81, height=29,
                     undo=True, bd=2, wrap="word")
tframe = tk.Listbox(sframe, width=25, height=26, font=('Roboto', 15),
                    state='disabled', disabledforeground='black',
                    bd=2)
fframe = ctk.CTkFrame(sframe, width=270, height=50, fg_color="#3B8ED0")
btn_save = ctk.CTkButton(fframe, width=15, height=15, image=img_save,
                         font=("Roboto", 15), text="", fg_color='gray86',
                         command=lambda: (file_saved(True)))
btn_refresh = ctk.CTkButton(fframe, width=15, height=15, fg_color='gray86',
                            font=("Roboto", 15), text="", image=img_refresh,
                            command=lambda: (display()))
btn_exit = ctk.CTkButton(fframe, width=15, height=15, fg_color='gray86',
                         font=("Roboto", 15), text="", image=img_close,
                         command=lambda: (wc.save_text(),
                                          wc.unactive_buttons(),
                                          wc.active_blank_tp(),
                                          wc.goto(blank_templates_page)))
btn_plus = ctk.CTkButton(fframe, width=15, height=15, fg_color='gray86',
                         font=("Roboto", 15), text="", image=img_plus,
                         command=lambda: ())
working_file = None


def editing_mode():
    frame.pack(side='right')
    sframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    textbox.place(relx=0, rely=0.5, anchor=tk.W)
    tframe.place(relx=1.0, rely=0.4668, anchor=tk.E)
    fframe.place(relx=1.0, rely=0.973, anchor=tk.E)
    btn_exit.place(relx=0.83, rely=0.40, anchor=tk.CENTER)
    btn_plus.place(relx=0.60666, rely=0.40, anchor=tk.CENTER)
    btn_refresh.place(relx=0.37666, rely=0.40, anchor=tk.CENTER)
    btn_save.place(relx=0.15, rely=0.40, anchor=tk.CENTER)
    update()

    global working_file
    if working_file is None:
        text_file = open('templates/ct_working_template.txt', "a")
        working_file = 'templates/ct_working_template.txt'
    else:
        text_file = open('templates/ct_working_template.txt', "r")
        text = text_file.read()
        textbox.insert(1.0, text)


# update page every 0.3 seconds to load new configuration
def update():
    highlight_brackets()
    save_ct_text()
    if saved is True:
        file_saved(True)
    root.after(200, update)


# display elements to fill
def display():
    tframe.config(state='normal')
    elements = re.findall(r'\{(.*?)\}', textbox.get("1.0", "end"))
    elements = list(dict.fromkeys(elements))
    tframe.delete(0, tk.END)
    for item in elements:
        tframe.insert(tk.END, item)
    tframe.config(state='disabled')


# highliters
def highlight_brackets():
    elements = re.findall(r'\{|\}', textbox.get("1.0", "end"))
    textbox.tag_configure("blue", foreground="#36719F")
    for element in elements:
        textbox.highlight_pattern(element, "blue")


saved = False


# save working file when changing tabs
def save_ct_text():
    with open("templates/ct_working_template.txt", "w") as f:
        f.write(str(textbox.get("0.0", "1.0")))
        f.close()


# save variables to json
def white_spaces_json(path):
    f = open(path, 'r')
    text = f.read()
    list_of_fillables = re.findall(r'\{(.*?)\}', text)
    dict = {}
    for i in list_of_fillables:
        dict[i] = ''
    return dict


# save template as
def save_template(name):
    global saved
    global bar_name
    bar_name = name.replace(" ", "_")

    with open(f"templates/blank_templates/{bar_name}.txt", "w") as f:
        f.write(str(textbox.get("1.0", "end")))
        f.close()

    dir_path = r'templates/blank_templates/'
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    list = []
    for f in res:
        dict = white_spaces_json(f"templates/blank_templates/{f}")
        list.append({f"{f}": dict})

    with open('templates/templates_data.json', 'w') as f:
        json.dump(list, f, indent=4)
    saved = True


# save created template window
def swindow(main):
    global window
    window = ctk.CTkToplevel(root)
    window.title("Save your created temlplate")
    window.geometry("400x120")
    window.resizable(False, False)
    window.transient(root)
    window.wait_visibility()
    window.grab_set()

    text = ctk.CTkLabel(window, text_color="#3B8ED0", font=("Roboto", 17),
                        text="Save template as:")
    entry = ctk.CTkEntry(window, width=350, height=35,
                         placeholder_text="Enter the name of template here",
                         font=("Roboto", 15))
    if main is False:
        button = ctk.CTkButton(window, text="Save and exit", fg_color="white",
                               width=200, height=30, text_color="#3B8ED0",
                               command=lambda: [save_template(entry.get()),
                                                root.destroy()])
    else:
        button = ctk.CTkButton(window, text="Save and continue",
                               fg_color="white", width=200, height=30,
                               text_color="#3B8ED0",
                               command=lambda: [save_template(entry.get()),
                                                window.destroy()])

    text.place(x=20, y=10)
    entry.place(x=20, y=40)
    button.place(x=100, y=85)


# if file already saved
def file_saved(main):
    if saved is False:
        swindow(main)
    else:
        save_template(bar_name)
        if main is False:
            root.destroy()


# message box for saving files
def questions_responses(response):
    if response is False:
        root.destroy()
    if response:
        try:
            window.destroy()
        except NameError:
            pass
        finally:
            file_saved(False)


def pop_message():
    if saved is True:
        root.destroy()
    else:
        response = messagebox.askyesnocancel("Quit",
                                             "Would you like to save your \
                                             created template?")
        questions_responses(response)


def ct_window_alert():
    count = int(len(textbox.get("1.0", 'end-1c')))
    if count != 0:
        if working_file is None:
            root.destroy()
        else:
            pop_message()
    else:
        root.destroy()
