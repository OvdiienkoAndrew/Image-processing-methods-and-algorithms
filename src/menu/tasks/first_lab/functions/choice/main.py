
def choice(main,label,file_path):
    from src.menu.tasks.first_lab.functions.choice_file.main import choice_file
    from src.menu.tasks.first_lab.functions.characteristics.main import characteristics
    from src.menu.tasks.first_lab.functions.task.main import task

    match label:
        case "Обрати зображення":
            choice_file(main, file_path)
        case "зчитати та вивести характеристики":
            characteristics(main, file_path)
        case "Індивідуальне завдання № 13":
            task(main, file_path)