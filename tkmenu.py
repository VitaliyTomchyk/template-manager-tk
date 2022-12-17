import customtkinter as ctk
from window import root
from window_config import open_sidebar
from tabs.fill_template_page import fill_template_page

def main():
    fill_template_page()
    return root.mainloop()

if __name__ == "__main__":
    main()
