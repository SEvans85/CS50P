import operator

word = input('Enter your expression: ')
expresion = word.split(' ')
print(expresion)
x = float(expresion[0])
y = expresion[1]
z = float(expresion[2])


if y == '+':
    y = operator.add(x, z)
elif y == '-':
    y = operator.sub(x, z)
elif y == '*':
    y = operator.mul(x, z)
elif y == '/':
    y = operator.truediv(x, z)
elif y== '%':
    y = operator.mod(x, z)
elif y == '^':
    y = operator.xor(x, z)


print(y)
