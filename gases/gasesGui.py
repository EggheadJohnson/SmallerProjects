from gases import *
from Tkinter import *

def handler(p1, p2, v1, v2, t1, t2, n1, n2):
    answerWindow = Toplevel()
    answerText = ''
    p1 = float(p1)
    p2 = float(p2)
    v1 = float(v1)
    v2 = float(v2)
    t1 = float(t1)
    t2 = float(t2)
    n1 = float(n1)
    n2 = float(n2)
    if n1 == n2 and [p1, p2, v1, v2, t1, t2].count(0) == 1:
        answerText = combined(p1, v1, t1, p2, v2, t2)
    elif p2 == 0 and v2 == 0 and t2 == 0 and n2 == 0 and [p1, v1, t1, n1].count(0) == 1:
        answerText = ideal(p1, v1, t1, n1)
    else:
        answerText = "Bad times"
    answer = Label(answerWindow, text=answerText)
    answer.pack()




root = Tk()


InitLabel = Label(root, text="Initial conditions")
InitVolText = Label(root, text="Volume")
InitVol = Entry(root)
InitVol.insert(0,0)
InitPressText = Label(root, text="Pressure")
InitPress = Entry(root)
InitPress.insert(0,0)
InitMolText = Label(root, text="Moles")
InitMol = Entry(root)
InitMol.insert(0,0)
InitTempText = Label(root, text="Temperature")
InitTemp = Entry(root)
InitTemp.insert(0,0)

FinalLabel = Label(root, text="Final conditions")
FinalVolText = Label(root, text="Volume")
FinalVol = Entry(root)
FinalVol.insert(0,0)
FinalPressText = Label(root, text="Pressure")
FinalPress = Entry(root)
FinalPress.insert(0,0)
FinalMolText = Label(root, text="Moles")
FinalMol = Entry(root)
FinalMol.insert(0,0)
FinalTempText = Label(root, text="Temperature")
FinalTemp = Entry(root)
FinalTemp.insert(0,0)

InitLabel.grid(row=0, columnspan=2)
InitVolText.grid(row=1)
InitVol.grid(row=1, column=1)
InitPressText.grid(row=2)
InitPress.grid(row=2, column=1)
InitMolText.grid(row=3)
InitMol.grid(row=3, column=1)
InitTempText.grid(row=4)
InitTemp.grid(row=4, column=1)

FinalLabel.grid(row=0, column=3)
FinalVolText.grid(row=1, column = 3)
FinalVol.grid(row=1, column=4)
FinalPressText.grid(row=2, column = 3)
FinalPress.grid(row=2, column=4)
FinalMolText.grid(row=3, column = 3)
FinalMol.grid(row=3, column=4)
FinalTempText.grid(row=4, column = 3)
FinalTemp.grid(row=4, column=4)

buttonGo = Button(root, text="Go!", command=lambda: handler(InitPress.get(), FinalPress.get(), InitVol.get(), FinalVol.get(), InitTemp.get(), FinalTemp.get(), InitMol.get(), FinalMol.get()))
buttonGo.grid(row=5, columnspan=4)

root.mainloop()
