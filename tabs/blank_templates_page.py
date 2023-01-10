import customtkinter as ctk
import tkinter as tk
import os
from window import root
from PIL import Image
import pyperclip


# images
img_copy = ctk.CTkImage(Image.open("images/icons-copy.png"), size=(20, 20))
img_edit = ctk.CTkImage(Image.open("images/icons-pen.png"), size=(20, 20))


frame = ctk.CTkFrame(root, width=1750, height=1080, border_width=1.5,
                     fg_color="#3B8ED0")
sframe = ctk.CTkFrame(frame, width=1200, height=710, border_width=0,
                      fg_color="#3B8ED0")


def blank_templates_page():
    frame.pack(side='right')
    sframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    templates()
    pass


def template_name(file):
    spaces = file.replace("_", " ")
    capitalized = spaces.capitalize()
    file_name = capitalized[:-4]
    return file_name


def back_to_file(template):
    bars = template.replace(" ", "_")
    lower = bars.lower()
    file = lower + ".txt"
    return file


def copy(file, textbox):
    textbox.configure(state="normal"),
    pyperclip.copy(open(f"templates/blank_templates/{file}", "r").read()),
    textbox.configure(state="disabled")    


def label_prop(labels):
    num = 0
    for label in labels:

        file = back_to_file(label.cget("text"))
        with open(f"templates/blank_templates/{file}") as t:
            text = t.read()

        title = ctk.CTkLabel(label, text=label.cget("text"),
                             width=200, height=15, fg_color="transparent",
                             font=("Roboto", 20), text_color="gray86")
        title.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

        textbox = ctk.CTkTextbox(label, font=("Roboto", 13), height=180,
                                 wrap="word")
        textbox.insert("0.0", text)
        textbox.configure(state="disabled")
        textbox.place(relx=0.5, rely=0.57, anchor=tk.CENTER)

        btn_copy = ctk.CTkButton(label, text="", image=img_copy,
                                 fg_color="#3B8ED0", bg_color="white",
                                 width=11, height=11,
                                 command=lambda: (copy(file, textbox)))
        btn_edit = ctk.CTkButton(label, text="", image=img_edit,
                                 fg_color="#3B8ED0", bg_color="white",
                                 width=11, height=11)
        btn_copy.place(relx=0.65, rely=0.92, anchor=tk.CENTER)
        btn_edit.place(relx=0.85, rely=0.92, anchor=tk.CENTER)
        num += 1


labels = []


def templates():
    del labels[:]
    t_num = 0
    count_x = 0
    count_y = 0
    for file in os.listdir("templates/blank_templates/"):
        if file.endswith(".txt"):
            file_name = template_name(file)
            labels.append(ctk.CTkLabel(sframe, text=file_name,
                                       width=200, height=210,
                                       fg_color="transparent"))
            x_pos = f"0.{1 + (count_x * 2)}"
            y_pos = f"0.{2 + (count_y * 3)}"
            labels[t_num].place(relx=float(x_pos), rely=float(y_pos),
                                anchor=tk.CENTER)
            t_num += 1
            if count_x < 4:
                count_x += 1
            else:
                count_x = 0
                count_y += 1
    label_prop(labels)
