

def rgb(main):
    from tkinter import filedialog
    from tkinter import messagebox
    import threading
    from src.menu.convert.functions.convert.rgb.do.main import do
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[
            ("Усі зображення", "*.bmp *.png *.gif *.tiff *jpg")
        ]
    )

    if not file_path:
        messagebox.showinfo("Попередження", "Файл не обрано або має валідну помилку в назві!")
        return

    main.start()
    threading.Thread(target=do, args=(main, file_path), daemon=True).start()

    return