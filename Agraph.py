from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import community
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


bgCol = "#392239"
fgCol = "#ac93ac"
#Testing networkx and importing test file
f = plt.Figure(figsize = (5,4), facecolor = bgCol)
a = f.add_subplot(111)
a.set_facecolor(fgCol)


path = 'c:/users/lucien/desktop/network_visualization/data/LesMiserables.gexf'
G = nx.read_gexf(path)
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos = pos, ax = a, with_labels=False)
xlim = a.get_xlim()
ylim = a.get_ylim()
plt.axis('off')
a.set_title('Circular Layout', fontsize = 30, color = "white")


#afficher la fenêtre principale
window = Tk()
window.title("A-graph")
window.geometry("1124x780")
window.minsize(1024, 720)
window.resizable(width=False, height=False)
#background color

window.config(background = bgCol)


#frame
frame = Frame(window, bg = bgCol, bd = 1, relief = SUNKEN)
toolbarFrame = Frame(master = window)


#Radiochoice (exclusive choice)
radioVals = ["1","2","3","4"]
radioText = ["Kamada", "Circular", "Spectral", "Shell"]
radioVar = StringVar()
radioVar.set(radioVals[0])
kamada = Radiobutton(frame, variable = radioVar, text = radioText[0], value = radioVals[0], bg = bgCol, fg = fgCol, font = "Courrier")
circular = Radiobutton(frame, variable = radioVar, text = radioText[1], value = radioVals[1], bg = bgCol, font = "Courrier",fg = fgCol)
spectral = Radiobutton(frame, variable = radioVar, text = radioText[2], value = radioVals[2], bg = bgCol, font = "Courrier",fg = fgCol)
shell = Radiobutton(frame, variable = radioVar, text = radioText[3], value = radioVals[3], bg = bgCol, font = "Courrier",fg = fgCol)
buttonHeight= 5
buttonWidth = 11
#kamada.configure(width = buttonWidth, height = buttonHeight)
#circular.configure(width = buttonWidth, height = buttonHeight)
#spectral.configure(width = buttonWidth, height = buttonHeight)
#shell.configure(width = buttonWidth, height = buttonHeight)
        

#Buttons
refreshButt = Button(frame, text = "Refresh",bg = fgCol, fg =bgCol,font = "Courrier, 20")   
loadButt = Button(frame, text = "Import",bg = fgCol, fg =bgCol,font = "Courrier, 20")
exitButton = Button(frame, text = "Exit", bg = fgCol, fg = bgCol, font = "Courrier, 20")
nextButton = Button(frame, text = "Next", bg = fgCol, fg = bgCol, font = "Courrier, 20")
prevButton = Button(frame, text = "Previous", bg = fgCol, fg = bgCol, font = "Courrier, 20")
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

#text entries
sizeEntry  = Entry(frame)
sizeInput = IntVar()
sizeInput.set(10)
filterEntry = Entry(frame)
filterInput = DoubleVar()
filterInput.set(5)

#deroulantes
optionData = ("Data1", "Data2", "Data3")
optionDataVar = StringVar()
optionDataVar.set(optionData[0])
optionsDataMenu = OptionMenu(frame, optionDataVar, *optionData)
optionsCombo1 = ttk.Combobox(frame, values = optionData)
optionsCombo1.current(0)

optionMetrics2 = ("met1", "met2", "met3")
optionMetricsVar2 = StringVar()
optionMetricsVar2.set(optionMetrics2[0])
optionsDataMenu2 = OptionMenu(frame, optionMetricsVar2, *optionMetrics2)
optionsCombo2 = ttk.Combobox(frame, values = optionMetrics2)
optionsCombo2.current(0)

optionMetrics3 = ("met1", "met2", "met3")
optionMetricsVar3 = StringVar()
optionMetricsVar3.set(optionMetrics3[0])
optionsDataMenu3 = OptionMenu(frame, optionMetricsVar3, *optionMetrics3)
optionsCombo3 = ttk.Combobox(frame, values = optionMetrics3)
optionsCombo3.current(0)

optionMetrics4 = ("met1", "met2", "met3")
optionMetricsVar4 = StringVar()
optionMetricsVar4.set(optionMetrics4[0])
optionsDataMenu4 = OptionMenu(frame, optionMetricsVar4, *optionMetrics4)
optionsCombo4 = ttk.Combobox(frame, values = optionMetrics4)
optionsCombo4.current(0)

optionMetrics5 = ("colset1", "colset2", "colset3")
optionMetricsVar5 = StringVar()
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

#GridSpacing
for i in range(0,21):
    frame.grid_columnconfigure(i, minsize = 49)
frame.grid_columnconfigure(13, minsize = 0)
    
for i in range(0,15):
    frame.grid_rowconfigure(i, minsize = 51)

#Gridlayout 
frame.grid(column = 0, row = 0, columnspan = 21, rowspan = 15, sticky = N + S + W + E)
kamada.grid(column = 1, row = 0, columnspan = 3, sticky = N + S + W + E)
circular.grid(column = 4, row = 0, columnspan = 3, sticky = N + S + W + E)
spectral.grid(column = 7, row = 0, columnspan = 3, sticky = N + S + W + E)
shell.grid(column = 10, row = 0, columnspan = 3, sticky = N + S + W + E)
optionsCombo1.grid(column = 14, row = 0, columnspan = 4, sticky = N + S + W + E)
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
canvas.get_tk_widget().grid(row=2, column=1, columnspan = 16, rowspan = 12,sticky = N + S + W + E)
canvas.draw()
#toolbar
toolbarFrame.grid(column = 0, row = 14, columnspan = 10)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)







window.mainloop()
