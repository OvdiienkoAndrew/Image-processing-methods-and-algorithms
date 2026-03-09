
if __name__ == '__main__':
    from src.models.main.main import Main
    from src.menu.convert.main import main_menu
    main = Main()
    main_menu(main)
    main.run()
