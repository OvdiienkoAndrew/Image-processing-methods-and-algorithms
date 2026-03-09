
def first_lab_menu(main,temp_file_path=None):
    from src.menu.tasks.first_lab.functions.choice.main import choice
    import tkinter
    file_path = temp_file_path
    main.clear()
    main.set_title("Перша лабораторна")

    labels = ["Обрати зображення",
              "зчитати та вивести характеристики",
              "Індивідуальне завдання № 13"
              ]
    buttons = []

    empty_height = round((main.get_height() - 50 * len(labels))/(len(labels)+1))

    for i,label in enumerate(labels):
        buttons.append(tkinter.Button(main.get_window(), text=label, command=lambda label=label: choice(main, label,file_path)))
        buttons[-1].place(x=(main.get_width()-round(main.get_width()*2/3))/2, y=empty_height*(i+1)+i*50,width=round(main.get_width()*2/3), height=50)

    main.update()