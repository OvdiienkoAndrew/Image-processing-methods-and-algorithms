

def choice(main, label):
    from src.menu.convert.functions.convert.binary.main import binary
    from src.menu.convert.functions.convert.monochrome.main import monochrome
    from src.menu.convert.functions.convert.rgb.main import rgb
    from src.menu.convert.functions.convert.bmp.main import bmp
    from src.menu.convert.functions.convert.png.main import png

    match label:
        case "Бінарне /двоколірне – глибина кольору 1 біт/піксель":
            binary(main)
        case "Монохромне/напівтонове – глибина кольору 8 біт/піксель":
            monochrome(main)
        case "Повноколірне TrueColor - глибина кольору – 24 біт/піксель":
            rgb(main)
        case ".bmp":
            bmp(main)
        case ".png":
            png(main)
