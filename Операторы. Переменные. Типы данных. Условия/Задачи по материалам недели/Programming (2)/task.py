# put your python code here
a = float(input())
b = float(input())
operand = input()
def default():
    return "Incorrect input!"

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    if (b == 0):
        return str("Деление на 0!")
    else:
        return a/b
def mod(a, b):
    if (b == 0):
        return str("Деление на 0!")
    else:
        return a % b
def pow(a, b):
    return a**b
def divInt(a, b):
    if (b == 0):
        return str("Деление на 0!")
    else:
        return a//b

operand_event = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mult,
    'mod': mod,
    'pow': pow,
    'div': divInt
}
try:
    result = operand_event[operand](a,b)
except KeyError as e:
    # можно также присвоить значение по умолчанию вместо бросания исключения
    raise ValueError('Undefined operand: {}'.format(e.args[0]))
print(result)
