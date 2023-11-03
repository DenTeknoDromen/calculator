# Siffer input
# Enkla beräkningar
# GUI med input

operators = ["+", "-", "/", "*", 
             "**", "%", "(", ")"]

def make_float(input):
    try:
        input = float(input)
    except Exception as e:
        input = None
        print("Wrong input")
    return input

def get_operand(inputs, operand):
    if operand == "+":
        inputs[0] += inputs[1]
    elif operand == "-":
        inputs[0] -= inputs[1]
    elif operand == "*":
        inputs[0] *= inputs[1]
    elif operand == "/":
        inputs[0] /= inputs[1]
    elif operand == "**":
        inputs[0] **= inputs[1]        
    elif operand == "%":
        inputs[0] %= inputs[1]        

    return inputs[0]

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


print(parse_input("55+55-5.5"))