

def do(main, file_path):
    from PIL import Image

    from tkinter import messagebox
    from src.menu.tasks.first_lab.functions.characteristics.result.main import result

    if not file_path:
        messagebox.showerror("Помилка","Файл не обрано!")
        main.end()
        return

    text = f"Файл: \"{file_path}\".\n\n\n"
    try:
        with Image.open(file_path) as img:
            text += f"Розмір у пікселях по горизонталі: {img.size[0]}.\n\n"
            text += f"Розмір у пікселях по вертикалі: {img.size[1]}.\n\n"
    except Exception as e:
        messagebox.showerror("Помилка",f"Не вдалося визначити розмір у пікселях по горизонталі та по вертикалі у файлі: \"{file_path}\"!\n\nПомилка: \"{e}\".")
        main.end()
        return

    try:
        with Image.open(file_path) as img:
            temp = {
                "1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24,
                "I": 32, "F": 32, "I;16": 16, "I;16L": 16, "I;16B": 16, "I;16S": 16,
                "RGB;16L": 48, "RGB;16B": 48, "RGBA;16L": 64, "RGBA;16B": 64,
                "LA": 16, "RGBX": 32, "RGBa": 32
            }.get(img.mode,"Невідомо")
            text += f"Глибина кольору: {temp}.\n\n"

    except Exception as e:
        messagebox.showerror("Помилка",f"Не вдалося визначити глибину кольору у файлі: \"{file_path}\"!\n\nПомилка: \"{e}\".")
        main.end()
        return

    try:
        with Image.open(file_path) as img:
            text += f"Кількість кольорів: {len(img.getcolors(maxcolors=img.size[0]*img.size[1]))}.\n\n"

    except Exception as e:
        messagebox.showerror("Помилка",f"Не вдалося визначити кількість кольорів у файлі: \"{file_path}\"!\n\nПомилка: \"{e}\".")
        main.end()
        return

    main.end()
    main.get_window().after(1, result, main, file_path,text)