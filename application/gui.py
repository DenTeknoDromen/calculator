from tkinter import*
from tkinter import ttk
from input_class import input
from main import operators, main

root = Tk()
root.title("Calculator")
root.resizable(False, False)
#root.geometry("380x500")

frame = ttk.Frame(root)
buttons = ttk.Frame(frame)
display = ttk.Frame(frame, borderwidth=5, relief="flat", width=200, height=100)

cnvs = Canvas(frame, width=370, height=150, background="White")
id = cnvs.create_text(370, 150, text="0", anchor="se", justify=LEFT, font="TkHeadingFont 41")

def set_display():
    num = i.main_str
    i.reset_font()
    for x in range(len(num)):
        if x % 4 == 0:
            i.font_size -= 4
    if len(num) == 0:
        num = "0"
        i.reset()
    cnvs.itemconfigure(id, text=num, font=f"TkHeadingFont {i.font_size}")

i = input()
def testone(indata):
    if len(i.main_str) < 24:
        i.main_str += indata
        set_display()
    print(i.main_str)
    
def functions(indata):
    if indata == "=":
        i.main_str = str(main(i.main_str))
        set_display()
    if indata == "CE":
        i.reset()
        set_display()
    if indata == "🡨":
        end = len(i.main_str) - 1
        i.main_str = i.main_str[0:end]  
        set_display()



x = 10
b0 = ttk.Button(buttons, padding=x, text="0", command=lambda a="0": testone(a))
b1 = ttk.Button(buttons, padding=x, text="1", command=lambda a="1": testone(a))
b2 = ttk.Button(buttons, padding=x, text="2", command=lambda a="2": testone(a))
b3 = ttk.Button(buttons, padding=x, text="3", command=lambda a="3": testone(a))
b4 = ttk.Button(buttons, padding=x, text="4", command=lambda a="4": testone(a))
b5 = ttk.Button(buttons, padding=x, text="5", command=lambda a="5": testone(a))
b6 = ttk.Button(buttons, padding=x, text="6", command=lambda a="6": testone(a))
b7 = ttk.Button(buttons, padding=x, text="7", command=lambda a="7": testone(a))
b8 = ttk.Button(buttons, padding=x, text="8", command=lambda a="8": testone(a))
b9 = ttk.Button(buttons, padding=x, text="9", command=lambda a="9": testone(a))

bplus = ttk.Button(buttons, padding=x, text="+", command=lambda a="+": testone(a))
bequals = ttk.Button(buttons, padding=x, text="=", command=lambda a="=": functions(a))
bminus = ttk.Button(buttons, padding=x, text="-", command=lambda a="-": testone(a))
bmulti = ttk.Button(buttons, padding=x, text="×", command=lambda a="×": testone(a))
bdiv = ttk.Button(buttons, padding=x, text="÷", command=lambda a="÷": testone(a))
bexpo = ttk.Button(buttons, padding=x, text="∧", command=lambda a="∧": testone(a))

bcomma = ttk.Button(buttons, padding=x, text=".", command=lambda a=".": testone(a))
bopen = ttk.Button(buttons, padding=x, text="(", command=lambda a="(": testone(a))
bclose = ttk.Button(buttons, padding=x, text=")", command=lambda a=")": testone(a))
bpi = ttk.Button(buttons, padding=x, text="π", command=lambda a="π": testone(a))

bback = ttk.Button(buttons, padding=x, text="🡨", command=lambda a="🡨": functions(a))
bclear = ttk.Button(buttons, padding=x, text="CE", command=lambda a="CE": functions(a))


frame.grid()
display.grid(row=0)
buttons.grid(column=0, row=1)
cnvs.grid(row=0)

row = 5
b0.grid(column=1, row=row)
bequals.grid(column=3, row=row)
bcomma.grid(column=2, row=row)

row = 4
b1.grid(column=0, row=row)
b2.grid(column=1, row=row)
b3.grid(column=2, row=row)
bplus.grid(column=3, row=row)

row = 3
b4.grid(column=0, row=row)
b5.grid(column=1, row=row)
b6.grid(column=2, row=row)
bminus.grid(column=3, row=row)

row = 2
b7.grid(column=0, row=row)
b8.grid(column=1, row=row)
b9.grid(column=2, row=row)
bmulti.grid(column=3, row=row)

row = 1
bdiv.grid(column=3,row=row)
bopen.grid(column=1, row=row)
bclose.grid(column=2, row=row)

row=0
bclear.grid(column=2, row=row)
bback.grid(column=3, row=row)
bexpo.grid(column=0, row=row)


root.mainloop()