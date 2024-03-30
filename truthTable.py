from itertools import product

def OR(a, b):
    return a or b

def AND(a, b):
    return a and b

def NOR(a, b):
    return not (a or b)

def NAND(a, b):
    return not (a and b)

def XOR(a, b):
    return a != b

def NOT(a):
    return not a

def is_valid_expression(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack


input_values = input("인풋을 입력해주세요 (예: A,B,C,D): ")
circuit = input("회로를 입력해주세요 (사용가능: AND, OR, NOR, NAND, XOR, NOT): ")


if not is_valid_expression(circuit):
    print("회로의 괄호가 올바르지 않습니다.")
    exit(0)


variables = input_values.split(',')

truth_table = []
for values in product([False, True], repeat=len(variables)):
    env = {var: val for var, val in zip(variables, values)}
    result = eval(circuit, {"__builtins__": None}, {**env, "AND": AND, "OR": OR, "NOR": NOR, "NAND": NAND, "XOR": XOR, "NOT": NOT})
    #truth_table.append((*values, result))
    truth_table.append([*(int(val) for val in values), int(result)])

for entry in truth_table:
    print(entry)

