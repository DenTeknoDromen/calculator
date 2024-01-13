import math
# GUI med input

# Negativa tal och exponenter funkar inte, lös med gui
# Math decimal/length check
# parantes implementation
# negativa tal implementation (parantes)

operators = ["+", "-", "/", "÷", "×", "^", 
             "**", "%", "(", ")"]


def make_float(input):
    for x in range(len(input)):
        try:
            input[x] = float(input[x])
        except Exception as e:
            if input[x] in operators:
                input[x] = str(input[x])
    return input


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

def parse_input(input):
    index = 0
    output = []
    max = len(input)
    for x in range(max):
        if input[x] in operators:
            output.append(input[index:x])
            output.append(input[x])
            index = x + 1
        if x == max - 1:
            output.append(input[index:max])
    return output


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

def edgecase(indata):
    if "π" in indata:
        i = indata.index("π")
        indata[i] = math.pi  
    return indata

def main(input):
    lst_input = parse_input(input)  # placeholder
    lst_input = edgecase(lst_input)
    lst_input = make_float(lst_input)
    output = get_operand(lst_input[0], lst_input[2], lst_input[1])
    output = parse_output(output)
    return output


# while True:
#     print(main(input("> ")))
