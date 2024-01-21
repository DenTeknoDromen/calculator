import math
import re
import decimal

# Negativa tal och exponenter funkar inte, lös med gui
# Math decimal/length check
# parantes implementation
# negativa tal implementation (parantes)

operators = ["^", "×", "÷", "+", "-"]

# Converts string input to list with numbers and operators as string
def parse_input(str_input):
    #re.findall("")
    lst_input = re.split("([^0-9π.])", str_input)
    while "" in lst_input:
         lst_input.remove("")

    return lst_input

# Checks for edgecases that needs to be handled before making calculations
def check_edgecases(indata):
    while "π" in indata:
        i = indata.index("π")
        indata[i] = decimal.Decimal(math.pi)
    return indata

# Converts string integers to float numbers
# Returns list with operators as string and numbers as float
def make_float(input):
    for x in range(len(input)):
        try:
            input[x] = decimal.Decimal((input[x]))
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
    
    return a


def make_calc(lst_input, symbol):
    if lst_input[0] in operators:
        lst_input.insert(0, 0)

    if lst_input[-1] in operators:
         lst_input.append(0)

    i = 1
    while i < len(lst_input):
        if (lst_input[i] == symbol):
            output = get_operand(lst_input[i-1], lst_input[i+1], lst_input[i])
            lst_input[i] = output
            lst_input.pop(i+1)
            lst_input.pop(i-1)
        else:
            i += 1

    return lst_input

# !!
def make_pemdas(lst_input):
    while "(" in lst_input:
        open = lst_input.index("(")
        closed = lst_input.index(")")
        lst_input[open] = make_pemdas(lst_input[open + 1:closed])
        del lst_input[open + 1:closed + 1]


    for a in operators:
        if len(lst_input) == 1:
            break
        make_calc(lst_input, a)
    return lst_input[0]

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
    try:
        lst_input = check_edgecases(lst_input)
        lst_input = make_float(lst_input)
        output = make_pemdas(lst_input)
        output = parse_output(output)
    except Exception as e:
        return "ERROR"
    return output

if __name__ == "__main__":
    print(main("((1+2)+(1+2))*4"))
