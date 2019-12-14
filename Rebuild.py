from tkinter import *
from tkinter import ttk

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os

class Agraph:
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # frame
        frame = Frame(window, bg=bgCol, bd=1, relief=SUNKEN)
        toolbarFrame = Frame(master=window)

        # Radiochoice (exclusive choice)
        radioVals = ["0", "1", "2", "3"]
        radioText = ["Kamada", "Circular", "Spectral", "Shell"]
        radioVar = StringVar(window)
        radioVar.set(radioVals[0])
        kamada = Radiobutton(frame, variable=radioVar, text=radioText[0], value=radioVals[0], bg=bgCol, fg=fgCol,
                             font="Courrier")
        circular = Radiobutton(frame, variable=radioVar, text=radioText[1], value=radioVals[1], bg=bgCol,
                               font="Courrier", fg=fgCol)
        spectral = Radiobutton(frame, variable=radioVar, text=radioText[2], value=radioVals[2], bg=bgCol,
                               font="Courrier", fg=fgCol)
        shell = Radiobutton(frame, variable=radioVar, text=radioText[3], value=radioVals[3], bg=bgCol, font="Courrier",
                            fg=fgCol)
        buttonHeight = 5
        buttonWidth = 11
        # kamada.configure(width = buttonWidth, height = buttonHeight)
        # circular.configure(width = buttonWidth, height = buttonHeight)
        # spectral.configure(width = buttonWidth, height = buttonHeight)
        # shell.configure(width = buttonWidth, height = buttonHeight)

        # Buttons
        refreshButt = Button(frame, text="Refresh", bg=fgCol, fg=bgCol, font="Courrier, 20", command=refreshPlot)
        loadButt = Button(frame, text="Import", bg=fgCol, fg=bgCol, font="Courrier, 20")
        exitButton = Button(frame, text="Exit", bg=fgCol, fg=bgCol, font="Courrier, 20")
        nextButton = Button(frame, text="Next", bg=fgCol, fg=bgCol, font="Courrier, 20")
        prevButton = Button(frame, text="Previous", bg=fgCol, fg=bgCol, font="Courrier, 20")
        buttHeight = 1
        buttWidth = 7
        # refreshButt.configure(width = buttWidth, height = buttHeight)
        # loadButt.configure(width = buttWidth, height = buttHeight)
        # exitButton.configure(width = buttWidth, height = buttHeight)

        # labels
        colorLabel = Label(frame, text="Color", fg=fgCol, bg=bgCol, font="Courrier, 20")
        sizeLabel = Label(frame, text="Size", fg=fgCol, bg=bgCol, font="Courrier, 20")
        filterLabel = Label(frame, text="Filter", fg=fgCol, bg=bgCol, font="Courrier, 20")
        layoutLabel = Label(frame, text="Layout : ", fg=fgCol, bg=bgCol, font="Courrier, 20")

        # text entries
        sizeEntry = Entry(frame)
        sizeInput = IntVar(window)
        sizeInput.set(10)
        filterEntry = Entry(frame)
        filterInput = DoubleVar(window)
        filterInput.set(5)

        # deroulantes
        optionData = ("Data1", "Data2", "Data3")
        optionDataVar = StringVar(window)
        optionDataVar.set(optionData[0])
        optionsDataMenu = OptionMenu(frame, optionDataVar, *optionData)
        optionsCombo1 = ttk.Combobox(frame, values=optionData)
        optionsCombo1.current(0)

        optionMetrics2 = ("met1", "met2", "met3")
        optionMetricsVar2 = StringVar(window)
        optionMetricsVar2.set(optionMetrics2[0])
        optionsDataMenu2 = OptionMenu(frame, optionMetricsVar2, *optionMetrics2)
        optionsCombo2 = ttk.Combobox(frame, values=optionMetrics2)
        optionsCombo2.current(0)

        optionMetrics3 = ("met1", "met2", "met3")
        optionMetricsVar3 = StringVar(window)
        optionMetricsVar3.set(optionMetrics3[0])
        optionsDataMenu3 = OptionMenu(frame, optionMetricsVar3, *optionMetrics3)
        optionsCombo3 = ttk.Combobox(frame, values=optionMetrics3)
        optionsCombo3.current(0)

        optionMetrics4 = ("met1", "met2", "met3")
        optionMetricsVar4 = StringVar(window)
        optionMetricsVar4.set(optionMetrics4[0])
        optionsDataMenu4 = OptionMenu(frame, optionMetricsVar4, *optionMetrics4)
        optionsCombo4 = ttk.Combobox(frame, values=optionMetrics4)
        optionsCombo4.current(0)

        optionMetrics5 = ("colset1", "colset2", "colset3")
        optionMetricsVar5 = StringVar(window)
        optionMetricsVar5.set(optionMetrics4[0])
        optionsDataMenu5 = OptionMenu(frame, optionMetricsVar5, *optionMetrics5)
        optionsCombo5 = ttk.Combobox(frame, values=optionMetrics5)
        optionsCombo5.current(0)

        # Canvas
        # =============================================================================
        # canvas = FigureCanvasTkAgg(f, master = frame)
        # canvas.show()
        # canvas.get_tk_widget().grid(column = 2, row = 1, columnspan = 12, rowspan = 8)
        #
        # =============================================================================
        canvas = FigureCanvasTkAgg(f, frame)
        canvas.draw()
        canvasWidget = canvas.get_tk_widget()


