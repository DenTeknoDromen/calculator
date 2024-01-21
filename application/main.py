import math
import re
import decimal

# Sorted in pemdas order
operators = ["^", "×", "÷", "+", "-"]

# Converts string input to list with numbers and operators as string
def parse_input(str_input):
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

# Converts string numbers to decimal type
# Returns list with operators as string and numbers as float
def change_type(input):
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

# Goes through current list and perfoms the current operator
def make_calc(lst_input, symbol):
    # Removes any empty instances of list
    if lst_input[0] in operators:
        lst_input.insert(0, 0)

    if lst_input[-1] in operators:
         lst_input.append(0)

    # Iterates through input list and calls get_operand when
    # current operator is used
    i = 1
    while i < len(lst_input):
        if (lst_input[i] == symbol):
            # Sends 'a' 'operator' 'b' to get_operand
            result = get_operand(lst_input[i-1], lst_input[i+1], lst_input[i])
            # Saves result in 'a' position and deletes the rest
            lst_input[i] = result
            lst_input.pop(i+1)
            lst_input.pop(i-1)
        else:
            i += 1

    return lst_input

# Sorts through input list according to pemdas
def make_pemdas(lst_input):
    # Calls make_pemdas recursively if a paranthesis is present in input list
    while "(" in lst_input:
        open = lst_input.index("(")
        closed = get_close(lst_input, open)
        lst_input[open] = make_pemdas(lst_input[open + 1:closed])
        del lst_input[open + 1:closed + 1]

    # Iterates though operators in pemdas order
    # Calls make_calc with current symbol
    for a in operators:
        if len(lst_input) == 1:
            break
        make_calc(lst_input, a)
    return lst_input[0]

# Returns the index for closing parenthesis for the opening parenthesis in input_list
def get_close(lst_input, open_index):
    paran = (lst_input[open_index])

    for i in range(1, len(lst_input)):
        if lst_input[i] == "(" or lst_input[i] == ")":
            paran += lst_input[i]
        if "()" in paran:
            paran = paran.replace("()","")
        if paran == "":
            return i
    return len(lst_input) - 1

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
    try:
        lst_input = check_edgecases(lst_input)
        lst_input = change_type(lst_input)
        output = make_pemdas(lst_input)
        output = parse_output(output)
    except Exception as e:
        return "ERROR"
    return output

if __name__ == "__main__":
    print(main("((1+2)+(1+2))×4"))
