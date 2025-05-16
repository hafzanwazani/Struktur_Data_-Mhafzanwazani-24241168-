# Logika: or, and, xor, not

# NOT
x = True
z = not x
print("Nilai dari z =", z)

print("\n********** AND ***********")
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)

x = True
y = False
z = x and y
print(x, 'and', y, '=', z)

x = False
y = True
z = x and y
print(x, 'and', y, '=', z)

x = False
y = False
z = x and y
print(x, 'and', y, '=', z)