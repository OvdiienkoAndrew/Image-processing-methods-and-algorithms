

def do(main, file_path):
    from PIL import Image
    from tkinter import messagebox

    if not file_path:
        messagebox.showerror("Помилка", "Файл не обрано!")
        main.end()
        return

    img = Image.open(file_path)
    pixels = img.load()

    width, height = img.size


    for i in range(4,width,20):
        for k in range(i, min(i + 6, width)):
            for j in range(height):
                pixels[k, j] = (185,239, 201, 255)


    img.save(f"{file_path[:file_path.rfind('.')]}_convert{file_path[file_path.rfind('.'):]}")

    main.end()
    return