


def choice_file(main,file_path):
    from tkinter import filedialog
    from tkinter import messagebox
    from src.menu.tasks.first_lab.main import first_lab_menu

    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[
            ("Усі зображення", "*.bmp *.png *.gif *.tiff *jpg")
        ]
    )

    if file_path:
        messagebox.showinfo("Повідомлення",f"Успішно завантаженний файл: \"{file_path}\"!")
    else:
        messagebox.showerror("Помилка","Файл не обрано!")

    main.get_window().after(1,first_lab_menu, main, file_path)