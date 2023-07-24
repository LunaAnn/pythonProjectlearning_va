for i in range (1, 10):
    for j in range (1, i+1):
        print(f'{j}x{i}={i*j} ', end='\t')
    print()
print('')


for i in range(9, 0, -1):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j} ', end='\t')
    print()
print('')


for i in range(1, 10):
    for k in range(9 - i):
        print("        ", end='')
    for j in range(i, 0, -1):
        print(f'{j}x{i}={i*j:<4}', end='')
    print()
print('')

for i in range(9, 0, -1):
    for k in range(9-i):
        print('        ', end='')
    for j in range(i, 0, -1):
        print(f'{j}x{i}={i*j: >2}', end='\t')
    print()
print('')

