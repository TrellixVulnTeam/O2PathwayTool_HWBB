from tkinter import *
from tkinter.messagebox import askokcancel
from tkinter import ttk

from objects.app import app
from objects.settings import Settings
from modules.menubar import *
from modules.notification import notification
from modules.panel_side import SidePanel
from modules.panel_details import DetailsPanel
from modules.panel_plotting import PlottingPanel

root = Tk()
root.title("O2 Pathway Tool")
root.geometry("1000x750")
root.pack_propagate(1)

app.root = root
app.strVars = []
app.intVars = []

# Load settings
settings = Settings()
app.settings = settings

# Mainframe
mainframe = ttk.Frame(root)
mainframe.pack(expand=TRUE, fill=BOTH)

# Menubar
menu = createMenu(root)

# Panels
sidePanel = SidePanel(mainframe)
app.sidePanel = sidePanel

notification.setParent(mainframe)

detailsPanel = DetailsPanel(mainframe)
app.detailsPanel = detailsPanel

plottingPanel = PlottingPanel(mainframe)
app.plottingPanel = plottingPanel

root.config(menu=menu)

def showAdvLayout():
    testContainer = app.testDetailModule.container
    envContainer = app.envDetailModule.frame
    projectContainer = app.projectDetailModule.container

    projectContainer.pack_forget()
    testContainer.pack_forget()
    envContainer.pack_forget()

    projectContainer.pack(side = LEFT, fill = BOTH, expand=TRUE)
    testContainer.pack(side = LEFT, fill = BOTH, expand=TRUE)
    envContainer.pack(side = LEFT, fill = BOTH, expand=TRUE)

def showBasicLayout():
    testContainer = app.testDetailModule.container
    envContainer = app.envDetailModule.frame
    projectContainer = app.projectDetailModule.container

    projectContainer.pack_forget()
    testContainer.pack_forget()
    envContainer.pack_forget()

    testContainer.pack(side = LEFT, fill = BOTH, expand=TRUE)

if app.getActiveMode() == 0:
    showBasicLayout()
else:
    showAdvLayout()

def on_closing():
    if askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == '__main__':
    root.mainloop()