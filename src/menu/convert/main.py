
def main_menu(main):
    import tkinter
    from src.menu.convert.functions.choice.main import choice

    main.clear()
    main.set_title("Конвертація")
    labels = ["Бінарне /двоколірне – глибина кольору 1 біт/піксель",
              "Монохромне/напівтонове – глибина кольору 8 біт/піксель",
              "Повноколірне TrueColor - глибина кольору – 24 біт/піксель",
              ".bmp",
              ".png"
              ]
    buttons = []

    empty_height = round((main.get_height() - 50 * len(labels))/(len(labels)+1))

    for i,label in enumerate(labels):
        buttons.append(tkinter.Button(main.get_window(), text=label, command=lambda label=label: choice(main, label)))
        buttons[-1].place(x=(main.get_width()-round(main.get_width()*2/3))/2, y=empty_height*(i+1)+i*50,width=round(main.get_width()*2/3), height=50)

    main.update()