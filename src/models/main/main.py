import tkinter
from tkinter import Tk, font

from src.menu.convert.main import main_menu
from src.menu.tasks.first_lab.main import first_lab_menu


class Main:
    def __init__(self):
        self.__window = Tk()
        self.__window.withdraw()
        self.__window.title("Кінокомпанія AndrOvdk (Овдієнко Андрій Володимирович ПА-22-2) презентує")
        self.__window.geometry("1500x800")
        self.__window.resizable(False, False)
        self.__menu_font = tkinter.font.Font(
            family=font.families()[0] if "Times New Roman" not in font.families() else "Times New Roman", size=24)
        self.__window.option_add("*Font", self.__menu_font)
        self.__window.protocol("WM_DELETE_WINDOW", self.__close)
        self.__window.configure(bg="white")

        self.__temp_window = Tk()
        self.__temp_window.withdraw()
        self.__temp_window.title("Загрузка")
        self.__temp_window.geometry("600x400")
        self.__temp_window.resizable(False, False)
        self.__temp_window.option_add("*Font", self.__menu_font)
        self.__temp_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.__temp_window.configure(bg="white")

        self.__temp_label = tkinter.Label(self.__temp_window, text="Працюю...", bg="white", fg="black",font = (self.__menu_font.actual("family"),42))
        self.__temp_label.place(x=100, y=175, width=400, height=50)

        self.__temp_window.update()

        self.__window.after(1, lambda: self.__window.deiconify())
        self.clear()


    def run(self):
        self.__window.mainloop()
        self.__temp_window.mainloop()

    def __close(self):
        self.__window.destroy()
        self.__temp_window.destroy()

    def clear(self):
        for widget in self.__window.winfo_children():
            widget.destroy()

        self.__window.configure(bg="white")

        menu_bar = tkinter.Menu(self.__window)

        file_menu = tkinter.Menu(self.__window, tearoff=0)
        file_menu.add_command(label="Конвертація", command=lambda: self.__window.after(1, main_menu, self),activebackground="darkgreen", activeforeground="white")
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=lambda: self.__window.after(1, self.__close),activebackground="darkgreen", activeforeground="white")
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        tasks_menu = tkinter.Menu(self.__window, tearoff=0)
        tasks_menu.add_command(label="1", command=lambda: self.__window.after(1, first_lab_menu,self), activebackground="darkgreen", activeforeground="white")
        menu_bar.add_cascade(label="Лабораторні", menu=tasks_menu)

        self.__window.config(menu=menu_bar)

        self.__window.update()

    def update(self):
        self.__window.update()

    def get_width(self):
        return self.__window.winfo_width()

    def get_height(self):
        return self.__window.winfo_height()

    def set_title(self, title):
        self.__window.title(title)

    def get_window(self):
        return self.__window

    def start(self):
        self.__window.withdraw()
        self.__temp_window.deiconify()

    def end(self):
        self.__window.after(0, lambda: self.__temp_window.withdraw())
        self.__window.after(0, lambda: self.__window.deiconify())
