from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.resizable(False, False)
#root.geometry("380x500")

frame = ttk.Frame(root)
buttons = ttk.Frame(frame)
display = ttk.Frame(frame, borderwidth=5, relief="flat", width=200, height=100)

cnvs = Canvas(frame, width=370, height=150, background="White")
id = cnvs.create_text(370, 150, text="12345678901", anchor="se", justify=LEFT, font="TkHeadingFont 41", tags=("input"))

check = True
def testone(check, input):
    print("Hejhopp")

x = 10
b0 = ttk.Button(buttons, padding=x, text="0", command=testone(check, 0))
b1 = ttk.Button(buttons, padding=x, text="1")
b2 = ttk.Button(buttons, padding=x, text="2")
b3 = ttk.Button(buttons, padding=x, text="3")
b4 = ttk.Button(buttons, padding=x, text="4")
b5 = ttk.Button(buttons, padding=x, text="5")
b6 = ttk.Button(buttons, padding=x, text="6")
b7 = ttk.Button(buttons, padding=x, text="7")
b8 = ttk.Button(buttons, padding=x, text="8")
b9 = ttk.Button(buttons, padding=x, text="9")

bplus = ttk.Button(buttons, padding=x, text="+")
bequals = ttk.Button(buttons, padding=x, text="=")
bminus = ttk.Button(buttons, padding=x, text="-")
bmulti = ttk.Button(buttons, padding=x, text="x")


frame.grid()
display.grid(row=0)
buttons.grid(column=0, row=1)
cnvs.grid(row=0)

b0.grid(column=1, row=4)
b1.grid(column=0, row=3)
b2.grid(column=1, row=3)
b3.grid(column=2, row=3)
b4.grid(column=0, row=2)
b5.grid(column=1, row=2)
b6.grid(column=2, row=2)
b7.grid(column=0, row=1)
b8.grid(column=1, row=1)
b9.grid(column=2, row=1)

bmulti.grid(column=3, row=1)
bminus.grid(column=3, row=2)
bplus.grid(column=3, row=3)
bequals.grid(column=3, row=4)

#lbl1.grid(column=0, row=0, columnspan=4, rowspan=2)

root.mainloop()