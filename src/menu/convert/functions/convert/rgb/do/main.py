
def do(main,file_path):
    from tkinter import messagebox
    from PIL import Image

    try:
        new_file_path = file_path[:file_path.rfind(".")] + "_rgb" + file_path[file_path.rfind("."):]
    except Exception as e:
        messagebox.showerror("Помилка", f"Файл не має крапки у назві: \"{e}\"")
        main.end()
        return
    try:
        img = Image.open(file_path).convert('RGB')
        img.save(new_file_path)
    except Exception as e:
        messagebox.showerror("Помилка", f"Файл не конвертовано: \"{e}\"")
        main.end()
        return

    main.end()
    return