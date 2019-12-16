from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os

#paths names
dirname = os.path.dirname(__file__)
dataOne = os.path.join(dirname, 'data/lesmiserables.gexf')
dataTwo = os.path.join(dirname, 'data/airlines-sample.gexf')
dataThree = os.path.join(dirname, 'data/WebAtlas_EuroSiS.gexf')
dirDic = {
    "Les miserables" : dataOne,
    "Airlines" : dataTwo,
    "Webatlas" : dataThree
}

#Color settings
bgCol = "#392239"
fgCol = "#ac93ac"

#Global variables
global fArray
fArray = [] #Array for figures

global fI
fI = 0 #counter for keeping track of current graph

global fCount
fCount = 0

#Global arguments
global toolbar
toolbar = None
global globalLayout
globalLayout = "0" #0 = kamada, 1 = circular, 2 = spectral, 3 = shell

global globalData
globalData = "path"

global globalImport
globalImport = dirDic["Les miserables"]

global globalColMet
globalColMet = 0 #metrics to be defined, but same principle as globalLayout

global globalColset
globalColset = "colorset"

global globalSizeMet
globalSizeMet = 0 #idem

global globalSize
globalSize = 10

global globalFilter
globalFilter = 0 #idem

global globalFilterThreshold
globalFilterThreshold = 0

global f
f = 0 #plot

global checkedImport
checkedImport = False

global globalImported
globalImported = "path"

global checkedLabel
checkedLabel = False

# Testing networkx and importing test file
f = plt.Figure(figsize = (5,4), facecolor = bgCol)
a = f.add_subplot(111)
a.set_facecolor(fgCol)
path = dataOne
G = nx.read_gexf(dataOne, relabel = True)
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos = pos, ax = a, with_labels=False)
xlim = a.get_xlim()
ylim = a.get_ylim()
plt.axis('off')
a.set_title('Circular', fontsize = 30, color = "white")
fCount = fCount + 1
fArray.append(f)

#####################
#Utility functions
#####################
#Import
def openFile():
    global globalImported
    globalImported = askopenfilename(parent = window)
    print(globalImported)

#Refresh global variables (take widget values)
def refreshGlobals():

    global globalLayout
    globalLayout = radioVar.get()

    global globalData
    globalData = optionsCombo1.get()

    global checkedLabel
    checkedLabel = useLabelChecked.get()

    global globalImport
    global checkedImport
    checkedImport = useImportChecked.get()
    print("checked : ", checkedImport)
    if(checkedImport == False):
        globalImport = dirDic[optionsCombo1.get()]
    if(checkedImport == True):
        globalImport = globalImported

    global globalColMet
    globalColMet = 0  #todo

    global globalColset
    globalColset = "colorset" #todo

    global globalSizeMet
    globalSizeMet = 0  # idem #todo

    global globalSize
    globalSize = 10 #todo

    global globalFilter
    globalFilter = 0  # todo

    global globalFilterThreshold
    globalFilterThreshold = 0 #todo

    #print(globalData) #Can use this line to print on console the variable you want


################
#Plot functions
################
#Main refresh
def refreshPlot():
    #counter
    global fCount
    fCount = fCount + 1
    global fI
    fI = fCount - 1

    #refreshing all parameters
    refreshGlobals()
    global canvasWidget
    canvasWidget.destroy()
    global f
    f = 0
    arg = globalLayout
    if (arg == "0"):
        f = drawKamada(globalImport, "Kamada-kawai", "white", 30, checkedLabel)
    if (arg == "1"):
        f = drawCircular(globalImport, "Circular", "white", 30, checkedLabel)
    if (arg == "2"):
        f = drawSpiral(globalImport, "Spiral", "white", 30, checkedLabel)
    if (arg == "3"):
        f = drawFruchterman(globalImport, "Fruchterman-reingold", "white", 30, checkedLabel)
    if (arg == "4"):
        f = drawPlanar(globalImport, "Planar", "white", 30, checkedLabel)
    #storing graph
    global fArray
    fArray.append(f)

    canvas = FigureCanvasTkAgg(f, frame)
    canvas.draw()
    canvasWidget = canvas.get_tk_widget()
    canvasWidget.grid(row=2, column=1, columnspan=16, rowspan=12, sticky=N + S + W + E)
    global toolbar
    toolbar.destroy()
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

def prevRefresh():
    global fI
    print(fI)
    if(fI >= 1):
        #Destroying canvas
        global canvasWidget
        canvasWidget.destroy()
        #Getting f prev graph
        global f
        f = fArray[fI - 1]
        #Changing canvas and toolbar
        canvas = FigureCanvasTkAgg(f, frame)
        canvas.draw()
        canvasWidget = canvas.get_tk_widget()
        canvasWidget.grid(row=2, column=1, columnspan=16, rowspan=12, sticky=N + S + W + E)
        global toolbar
        toolbar.destroy()
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        fI = fI - 1
    else:
        messagebox.showerror(title="Agraph", message="There is no previous graph.")

def nextRefresh():
    global fI
    global fCount
    print(fI)
    if(fI < fCount-1):
        #Destroying canvas
        global canvasWidget
        canvasWidget.destroy()
        #Getting f prev graph
        global f
        f = fArray[fI + 1]
        #Changing canvas and toolbar
        canvas = FigureCanvasTkAgg(f, frame)
        canvas.draw()
        canvasWidget = canvas.get_tk_widget()
        canvasWidget.grid(row=2, column=1, columnspan=16, rowspan=12, sticky=N + S + W + E)
        global toolbar
        toolbar.destroy()
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        fI = fI + 1
    else:
        messagebox.showerror(title="Agraph", message="There is no next graph.")


###########################################################################
#The 4 functions below return f, a Figure that is then drawn on the canvas.
#Circular
def drawCircular(dataPath, titleString = "Title", color = "white", fontSize = 30, labels = False):
    global f
    f = plt.Figure(figsize=(5,4), facecolor=bgCol)
    a = f.add_subplot(111)
    a.set_facecolor(fgCol)
    G = nx.read_gexf(dataPath, relabel=True)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos = pos, ax = a, with_labels = labels)
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    plt.axis('off')
    a.set_title(titleString, fontsize = fontSize, color = color)
    return f

#Kamada
def drawKamada(dataPath, titleString = "Title", color = "white", fontSize = 30, labels = False):
    global f
    f = plt.Figure(figsize=(5,4), facecolor=bgCol)
    a = f.add_subplot(111)
    a.set_facecolor(fgCol)
    G = nx.read_gexf(dataPath, relabel = True)
    pos = nx.kamada_kawai_layout(G)
    nodeList = list(G.nodes)
    degreeList = G.degree
    nx.draw_networkx(G, pos = pos, ax = a, with_labels = labels)
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    plt.axis('off')
    a.set_title(titleString, fontsize = fontSize, color = color)
    return f

def drawFruchterman(dataPath, titleString="Title", color="white", fontSize=30, labels=False):
    global f
    f = plt.Figure(figsize=(5, 4), facecolor=bgCol)
    a = f.add_subplot(111)
    a.set_facecolor(fgCol)
    G = nx.read_gexf(dataPath, relabel = True)
    pos = nx.fruchterman_reingold_layout(G)
    nx.draw_networkx(G, pos=pos, ax=a, with_labels=labels)
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    plt.axis('off')
    a.set_title(titleString, fontsize=fontSize, color=color)
    return f


#Spectral
def drawSpiral(dataPath, titleString = "Title", color = "white", fontSize = 30, labels = False):
    global f
    f = plt.Figure(figsize=(5,4), facecolor=bgCol)
    a = f.add_subplot(111)
    a.set_facecolor(fgCol)
    G = nx.read_gexf(dataPath, relabel = True)
    pos = nx.drawing.spiral_layout(G)
    nx.draw_networkx(G, pos = pos, ax = a, with_labels = labels)
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    plt.axis('off')
    a.set_title(titleString, fontsize = fontSize, color = color)
    return f

#Shell
def drawPlanar(dataPath, titleString = "Title", color = "white", fontSize = 30, labels = False):
    global f
    f = plt.Figure(figsize=(5,4), facecolor=bgCol)
    a = f.add_subplot(111)
    a.set_facecolor(fgCol)
    G = nx.read_gexf(dataPath, relabel = True)
    pos = nx.drawing.planar_layout(G)
    nx.draw_networkx(G, pos = pos, ax = a, with_labels = labels)
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    plt.axis('off')
    a.set_title(titleString, fontsize = fontSize, color = color)
    return f


#Default graph to be displayed
fCirc = drawCircular(dataOne, "Circular", "white", 30, False)


#####################
#Main window config #
#####################

#Show main window
window = Tk()
window.title("A-graph")
window.geometry("1124x780")
window.minsize(1024, 720)
window.resizable(width=False, height=False)

#background color
window.config(background = bgCol)

#################
#Widgets
#################

#frame
frame = Frame(window, bg = bgCol, bd = 1, relief = SUNKEN)
toolbarFrame = Frame(master = window)

#Radiochoice (exclusive choice)
radioVals = ["0","1","2","3","4"]
radioText = ["Kamada", "Circular", "Spiral", "Fruchterman", "Planar"]
radioVar = StringVar(window)
radioVar.set(radioVals[0])
kamada = Radiobutton(frame, variable = radioVar, text = radioText[0], value = radioVals[0], bg = bgCol, fg = fgCol, font = "Courrier")
circular = Radiobutton(frame, variable = radioVar, text = radioText[1], value = radioVals[1], bg = bgCol, font = "Courrier",fg = fgCol)
spectral = Radiobutton(frame, variable = radioVar, text = radioText[2], value = radioVals[2], bg = bgCol, font = "Courrier",fg = fgCol)
fruchterman = Radiobutton(frame, variable = radioVar, text = radioText[3], value = radioVals[3], bg = bgCol, font = "Courrier",fg = fgCol)
planar = Radiobutton(frame, variable = radioVar, text = radioText[4], value = radioVals[4], bg = bgCol, font = "Courrier",fg = fgCol)
buttonHeight= 5
buttonWidth = 11
#kamada.configure(width = buttonWidth, height = buttonHeight)
#circular.configure(width = buttonWidth, height = buttonHeight)
#spectral.configure(width = buttonWidth, height = buttonHeight)
#shell.configure(width = buttonWidth, height = buttonHeight)


#Buttons
refreshButt = Button(frame, text = "Refresh",bg = fgCol, fg =bgCol,font = "Courrier, 20", command=refreshPlot)
loadButt = Button(frame, text = "Import",bg = fgCol, fg =bgCol,font = "Courrier, 20", command = openFile)
exitButton = Button(frame, text = "Exit", bg = fgCol, fg = bgCol, font = "Courrier, 20")
nextButton = Button(frame, text = "Next", bg = fgCol, fg = bgCol, font = "Courrier, 20", command = nextRefresh)
prevButton = Button(frame, text = "Previous", bg = fgCol, fg = bgCol, font = "Courrier, 20", command = prevRefresh)
buttHeight = 1
buttWidth = 7
#refreshButt.configure(width = buttWidth, height = buttHeight)
#loadButt.configure(width = buttWidth, height = buttHeight)
#exitButton.configure(width = buttWidth, height = buttHeight)


#labels
colorLabel = Label(frame, text = "Color",fg = fgCol, bg =bgCol,font = "Courrier, 20")
sizeLabel = Label(frame, text = "Size",fg = fgCol, bg =bgCol,font = "Courrier, 20")
filterLabel = Label(frame, text = "Filter",fg = fgCol, bg =bgCol,font = "Courrier, 20")
layoutLabel = Label(frame, text = "Layout : ",fg = fgCol, bg =bgCol,font = "Courrier, 20")

#Checkbutton
global useImportChecked
useImportChecked = BooleanVar(window)
useImportCheck = Checkbutton(frame, text = "Use import ", variable = useImportChecked, background = bgCol, fg = fgCol, activebackground = bgCol, onvalue = True)
global useLabelChecked
useLabelChecked = BooleanVar(window)
useLabelCheck = Checkbutton(frame, text = "Use labels", variable = useLabelChecked, background = bgCol, fg = fgCol, activebackground = bgCol, onvalue = True)

#text entries
sizeEntry  = Entry(frame)
sizeInput = IntVar(window)
sizeInput.set(10)
filterEntry = Entry(frame)
filterInput = DoubleVar(window)
filterInput.set(5)

#deroulantes
optionData = ("Les miserables", "Airlines", "Webatlas")
optionDataVar = StringVar(window)
optionDataVar.set(optionData[0])
optionsDataMenu = OptionMenu(frame, optionDataVar, *optionData)
optionsCombo1 = ttk.Combobox(frame, values = optionData)
optionsCombo1.current(0)

optionMetrics2 = ("met1", "met2", "met3")
optionMetricsVar2 = StringVar(window)
optionMetricsVar2.set(optionMetrics2[0])
optionsDataMenu2 = OptionMenu(frame, optionMetricsVar2, *optionMetrics2)
optionsCombo2 = ttk.Combobox(frame, values = optionMetrics2)
optionsCombo2.current(0)

optionMetrics3 = ("met1", "met2", "met3")
optionMetricsVar3 = StringVar(window)
optionMetricsVar3.set(optionMetrics3[0])
optionsDataMenu3 = OptionMenu(frame, optionMetricsVar3, *optionMetrics3)
optionsCombo3 = ttk.Combobox(frame, values = optionMetrics3)
optionsCombo3.current(0)

optionMetrics4 = ("met1", "met2", "met3")
optionMetricsVar4 = StringVar(window)
optionMetricsVar4.set(optionMetrics4[0])
optionsDataMenu4 = OptionMenu(frame, optionMetricsVar4, *optionMetrics4)
optionsCombo4 = ttk.Combobox(frame, values = optionMetrics4)
optionsCombo4.current(0)

optionMetrics5 = ("colset1", "colset2", "colset3")
optionMetricsVar5 = StringVar(window)
optionMetricsVar5.set(optionMetrics4[0])
optionsDataMenu5 = OptionMenu(frame, optionMetricsVar5, *optionMetrics5)
optionsCombo5 = ttk.Combobox(frame, values = optionMetrics5)
optionsCombo5.current(0)

#Canvas
# =============================================================================
# canvas = FigureCanvasTkAgg(f, master = frame)
# canvas.show()
# canvas.get_tk_widget().grid(column = 2, row = 1, columnspan = 12, rowspan = 8)
#
# =============================================================================
canvas = FigureCanvasTkAgg(f, frame)
canvas.draw()
canvasWidget = canvas.get_tk_widget()

##############
#GridSpacing
##############
for i in range(0,21):
    frame.grid_columnconfigure(i, minsize = 49)
frame.grid_columnconfigure(13, minsize = 0)

for i in range(0,15):
    frame.grid_rowconfigure(i, minsize = 51)
#########################
#Gridlayout  Configure
#########################
frame.grid(column = 0, row = 0, columnspan = 21, rowspan = 15, sticky = N + S + W + E)
kamada.grid(column = 1, row = 0, columnspan = 3, sticky = N + S + W + E)
circular.grid(column = 4, row = 0, columnspan = 3, sticky = N + S + W + E)
spectral.grid(column = 7, row = 0, columnspan = 3, sticky = N + S + W + E)
fruchterman.grid(column = 10, row = 0, columnspan = 3, sticky = N + S + W + E)
optionsCombo1.grid(column = 14, row = 0, columnspan = 4, sticky = N + S + W + E)
useImportCheck.grid(column = 16, row = 1, columnspan = 2)
useLabelCheck.grid(column = 14, row = 1, columnspan = 2)
refreshButt.grid(column = 19, row = 0, columnspan = 3, sticky = N + S + W + E)
loadButt.grid(column = 19, row = 1, columnspan = 3, sticky = N + S + W + E)
colorLabel.grid(column = 19, row = 3, columnspan = 3, sticky = N + S + W + E)
optionsCombo2.grid(column = 19, row = 4, columnspan = 3, sticky = N + S + W + E)
optionsCombo5.grid(column = 19, row = 5, columnspan = 3, sticky = N + S + W + E)
sizeLabel.grid(column = 19, row = 6, columnspan = 3, sticky = N + S + W + E)
optionsCombo3.grid(column = 19, row = 7, columnspan = 3, sticky = N + S + W + E)
sizeEntry.grid(column = 19, row = 8, columnspan = 3, sticky = N + S + W + E)
filterLabel.grid(column = 19, row = 9, columnspan = 3, sticky = N + S + W + E)
optionsCombo4.grid(column = 19, row = 10, columnspan = 3, sticky = N + S + W + E)
filterEntry.grid(column = 19, row = 11, columnspan = 3, sticky = N + S + W + E)
prevButton.grid(column = 15, row = 14, columnspan = 2, sticky = N + S + W + E)
nextButton.grid(column = 17, row = 14, columnspan = 2, sticky = N + S + W + E)
layoutLabel.grid(column = 0, row = 0, columnspan = 1, sticky = N + S + W + E)
canvasWidget.grid(row=2, column=1, columnspan = 16, rowspan = 12,sticky = N + S + W + E)
canvas.draw()
#toolbar
toolbarFrame.grid(column = 0, row = 14, columnspan = 10)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

#print(radioVar)
window.mainloop()