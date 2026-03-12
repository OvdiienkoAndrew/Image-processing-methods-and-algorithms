import multiprocessing
import numpy as np
from PIL import Image
from tkinter import messagebox

def proces_1(file_path,array,width):

    mask = array.mean(axis=2) < 128
    array[mask,:] = (0, 255, 0)
    array[~mask,:] = (255, 255, 255)

    for i in range(4,width,20):
        array[:,i:i+5] = (255,255,0)

    img = Image.fromarray(array)

    img.save(f"{file_path[:file_path.rfind('.')]}_such_binary{file_path[file_path.rfind('.'):]}")


def proces_2(file_path,array,width):

    middle = ((array[:, :,0].astype(int) + array[:, :,2].astype(int))//2).astype(int)

    array[:, :,0] = middle
    array[:, :,1] = 255
    array[:, :,2] = middle


    for i in range(4, width, 20):
        array[:, i:i + 5] = (255, 255, 0)

    img = Image.fromarray(array)


    img.save(f"{file_path[:file_path.rfind('.')]}_such_2_middle{file_path[file_path.rfind('.'):]}")


def proces_3(file_path,array,width):

    middle = array.mean(axis=2)

    array[:, :, 0] = middle
    array[:, :, 1] = 255
    array[:, :, 2] = middle

    for i in range(4, width, 20):
        array[:, i:i + 5] = (255, 255, 0)

    img = Image.fromarray(array)

    img.save(f"{file_path[:file_path.rfind('.')]}_such_3_middle{file_path[file_path.rfind('.'):]}")


def do(main, file_path):

    if not file_path:
        messagebox.showerror("Помилка", "Файл не обрано!")
        main.end()
        return

    img = Image.open(file_path)

    array = np.array(img)

    p1 = multiprocessing.Process(target=proces_1, args=(file_path,array,array.shape[1]))
    p2 = multiprocessing.Process(target=proces_2, args=(file_path,array,array.shape[1]))
    p3 = multiprocessing.Process(target=proces_3, args=(file_path,array,array.shape[1]))


    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


    main.end()
    return