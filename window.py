import customtkinter as ctk


# create a window
root = ctk.CTk(fg_color="#3B8ED0")
root.title("TM")
root.resizable(False, False)
root.geometry("1580x720+100+100")
root.config(cursor="top_left_arrow")


# window appearance
ctk.set_default_color_theme('custom-theme.json')
