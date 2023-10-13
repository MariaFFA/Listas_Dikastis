x = int(input())
z = int(input())

d_h = ((x - 34)**2 +(z - 220)**2)**(1/2)
d_k = ((x - 0)**2 +(z - 0)**2)**(1/2)
d_s = ((x - 140)**2 +(z - 456)**2)**(1/2)

print(f'Distancia para Hogsmeade: {d_h:.2f}')
print(f'Distancia para Kakariko: {d_k:.2f}')
print(f'Distancia para Solitude: {d_s:.2f}')