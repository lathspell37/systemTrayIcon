import pystray
import PIL.Image

image = PIL.Image.open("galatasaray.png")


def on_clicked(icon,item):
    if str(item) == "Say Hello":
        print("Hello World")
    elif str(item) == "Exit":
        icon.stop()   
    elif str(item) == "Submenu 1":
        print("Sub 1")
    else:
        print("Not implemented yet!")    


icon = pystray.Icon("Cimbom", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello",on_clicked),
    pystray.MenuItem("Exit",on_clicked),
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Submenu 1", on_clicked),
        pystray.MenuItem("Submenu 2", on_clicked)
    ))
))    

icon.run()