import math
import re

# Negativa tal och exponenter funkar inte, lös med gui
# Math decimal/length check
# parantes implementation
# negativa tal implementation (parantes)

operators = ["+", "-", "/", "÷", "×", "^", 
             "**", "%", "(", ")"]

# Converts string input to list with numbers and operators as string
def parse_input(str_input):
    lst_input = re.split("([^0-9π.])", str_input)
    if lst_input[0] == "":
        lst_input[0] = "0"

    if lst_input[-1] == "":
         lst_input[-1] = "0"

    return lst_input

# Checks for edgecases that needs to be handled before making calculations
def check_edgecases(indata):
    if "π" in indata:
        i = indata.index("π")
        indata[i] = math.pi  
    return indata

# Converts string integers to float numbers
# Returns list with operators as string and numbers as float
def make_float(input):
    for x in range(len(input)):
        try:
            input[x] = float(input[x])
        except Exception as e:
            if input[x] in operators:
                input[x] = str(input[x])
    return input

# Makes calulations according to operators
def get_operand(a, b, operand):
    if operand == "+":
        a += b
    elif operand == "-":
        a -= b
    elif operand == "×":
        a *= b
    elif operand == "÷":
        a /= b
    elif operand == "^":
        a **= b
    elif operand == "%":
        a %= b

    # Math decimalcheck här 
    return a


def make_calc(lst_input):
    output = lst_input[0]
    for i in range(2, len(lst_input), 2):
        output = get_operand(output, lst_input[i], lst_input[i-1])
    return output

# Converts list to string for output
def parse_output(indata):
    try:
        if int(indata) == float(indata):
            output = int(indata)
        else:
            output = float(indata)
    except Exception as e:
        print("Det här är fel")
        output = str(indata)
    return output

def main(input):
    lst_input = parse_input(input)
    print(lst_input)
    lst_input = check_edgecases(lst_input)
    lst_input = make_float(lst_input)
    output = make_calc(lst_input)
    output = parse_output(output)
    return output

if __name__ == "__main__":
    print(main("5÷5+5"))
