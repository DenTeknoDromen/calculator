from tkinter import*
from tkinter import ttk
from input_class import input
from main import operators, main

root = Tk()
root.title("Calculator")
root.resizable(False, False)

frame = ttk.Frame(root)
buttons = ttk.Frame(frame)
display = ttk.Frame(frame, borderwidth=5, relief="flat", width=200, height=100)

cnvs = Canvas(frame, width=370, height=150, background="White")
id = cnvs.create_text(370, 150, text="0", anchor="se", justify=LEFT, font="TkHeadingFont 41")

# Updates the screen on the calculator
def set_display():
    num = i.main_str
    
    # Resets font size
    i.reset_font()
    # Lowers fontsize for longer input
    for x in range(len(num)):
        if x % 4 == 0:
            i.font_size -= 4
    # Displays zero if input is empty
    if len(num) == 0:
        num = "0"
        i.reset()
    # Updates tkinter object
    cnvs.itemconfigure(id, text=num, font=f"TkHeadingFont {i.font_size}")

# Gets input from buttons
# Gets called on each buttonpress
i = input()
def get_input(indata):
    # Checks if number of symbols is lower than max
    if len(i.main_str) < 24:
        i.main_str += indata
        set_display()   #Updates screen for every buttonpress
    
# Used for special functions suchas clear and equals
def functions(indata):
    # Calls the main function with the input as string to be calculated
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


# Initializes buttons for numbers and symbols
padding = 10    # Changes padding for all buttons
btn_zero = ttk.Button(buttons, padding=padding, text="0", command=lambda a="0": get_input(a))
btn_one = ttk.Button(buttons, padding=padding, text="1", command=lambda a="1": get_input(a))
btn_two = ttk.Button(buttons, padding=padding, text="2", command=lambda a="2": get_input(a))
btn_three = ttk.Button(buttons, padding=padding, text="3", command=lambda a="3": get_input(a))
btn_four = ttk.Button(buttons, padding=padding, text="4", command=lambda a="4": get_input(a))
btn_five = ttk.Button(buttons, padding=padding, text="5", command=lambda a="5": get_input(a))
btn_six = ttk.Button(buttons, padding=padding, text="6", command=lambda a="6": get_input(a))
btn_seven = ttk.Button(buttons, padding=padding, text="7", command=lambda a="7": get_input(a))
btn_eight = ttk.Button(buttons, padding=padding, text="8", command=lambda a="8": get_input(a))
btn_nine = ttk.Button(buttons, padding=padding, text="9", command=lambda a="9": get_input(a))

btn_plus = ttk.Button(buttons, padding=padding, text="+", command=lambda a="+": get_input(a))
btn_equals = ttk.Button(buttons, padding=padding, text="=", command=lambda a="=": functions(a))
btn_minus = ttk.Button(buttons, padding=padding, text="-", command=lambda a="-": get_input(a))
btn_multi = ttk.Button(buttons, padding=padding, text="×", command=lambda a="×": get_input(a))
btn_div = ttk.Button(buttons, padding=padding, text="÷", command=lambda a="÷": get_input(a))
btn_expo = ttk.Button(buttons, padding=padding, text="^", command=lambda a="^": get_input(a))

btn_comma = ttk.Button(buttons, padding=padding, text=".", command=lambda a=".": get_input(a))
btn_paranopen = ttk.Button(buttons, padding=padding, text="(", command=lambda a="(": get_input(a))
btn_paranclose = ttk.Button(buttons, padding=padding, text=")", command=lambda a=")": get_input(a))
btn_pi = ttk.Button(buttons, padding=padding, text="π", command=lambda a="π": get_input(a))

btn_back = ttk.Button(buttons, padding=padding, text="🡨", command=lambda a="🡨": functions(a))
btn_clear = ttk.Button(buttons, padding=padding, text="CE", command=lambda a="CE": functions(a))

# Creates grid for UI
frame.grid()
display.grid(row=0)
buttons.grid(column=0, row=1)
cnvs.grid(row=0)

# Places buttons on grid
row = 5     # Shorthands for changing row number below
btn_zero.grid(column=1, row=row)
btn_equals.grid(column=3, row=row)
btn_comma.grid(column=2, row=row)

row = 4
btn_one.grid(column=0, row=row)
btn_two.grid(column=1, row=row)
btn_three.grid(column=2, row=row)
btn_plus.grid(column=3, row=row)

row = 3
btn_four.grid(column=0, row=row)
btn_five.grid(column=1, row=row)
btn_six.grid(column=2, row=row)
btn_minus.grid(column=3, row=row)

row = 2
btn_seven.grid(column=0, row=row)
btn_eight.grid(column=1, row=row)
btn_nine.grid(column=2, row=row)
btn_multi.grid(column=3, row=row)

row = 1
btn_div.grid(column=3,row=row)
btn_paranopen.grid(column=1, row=row)
btn_paranclose.grid(column=2, row=row)
btn_pi.grid(column=0, row=row)

row=0
btn_clear.grid(column=2, row=row)
btn_back.grid(column=3, row=row)
btn_expo.grid(column=0, row=row)


root.mainloop()