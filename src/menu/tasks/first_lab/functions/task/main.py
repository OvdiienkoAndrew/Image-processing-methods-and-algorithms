

def task(main,file_path):
    import threading
    from src.menu.tasks.first_lab.functions.task.do.main import do

    main.start()
    threading.Thread(target=do, args=(main, file_path), daemon=True).start()
