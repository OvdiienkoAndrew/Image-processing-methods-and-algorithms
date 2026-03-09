
def result(main, file_path, msg):
    import tkinter
    from src.menu.tasks.first_lab.main import first_lab_menu
    main.clear()

    text = tkinter.Text(main.get_window(), bg="white", fg="black", wrap="word", borderwidth=1, relief="solid")
    text.insert("1.0", msg)

    back_button = tkinter.Button(main.get_window(), text="←",
                                 command=lambda: main.get_window().after(1, first_lab_menu, main, file_path),
                                 bg="white", fg="black", activebackground="darkgreen", activeforeground="white")
    back_button.place(x=10, y=10)

    text.place(x=(main.get_width() - text.winfo_width()) / 2,
               y=(main.get_height() - text.winfo_height()) / 2,
               width=main.get_width() * 9 / 10,
               height=main.get_height() * 9 / 10)
    main.update()
    text.place(x=(main.get_width() - text.winfo_width()) / 2,
               y=(main.get_height() - text.winfo_height()) / 2,
               width=main.get_width() * 9 / 10,
               height=main.get_height() * 9 / 10)
    main.update()


