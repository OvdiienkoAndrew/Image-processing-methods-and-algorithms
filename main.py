from tkinter import filedialog

import numpy as np
from PIL import Image

if __name__ == '__main__':
    # from src.models.main.main import Main
    # from src.menu.convert.main import main_menu
    # main = Main()
    # main_menu(main)
    # main.run()
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[
            ("Усі зображення", "*.bmp *.png *.gif *.tiff *jpg")
        ]
    )
    img = Image.open(file_path)

    array = np.array(img)

    middle = array.mean(axis=2)

    array[:, :, 0] = middle
    array[:, :, 1] = middle
    array[:, :, 2] = middle

    img = Image.fromarray(array)

    img.save(f"{file_path[:file_path.rfind('.')]}_demo{file_path[file_path.rfind('.'):]}")




# синий негатив
# array[:, :, 0] = 255-middle
# array[:, :, 1] = 255-middle
# array[:, :, 2] = 255

# обычное но с накладкой сверху желтого и синего
# array[:, :, 0] = middle
# array[:, :, 1] = middle
# array[:, :, 2] = 128

# сине жолтий
# array[:, :, 0] = middle
# array[:, :, 1] = middle
# array[:, :, 2] = 255-middle

# желто синий
# array[:, :, 0] = 255-middle
# array[:, :, 1] = 255-middle
# array[:, :, 2] = middle