a = int(input())
l = int(input())
p = int(input())
h = int(input())
d_a = a*h
d_l = l*h
d_p = p*h
x = (d_a + d_l + (abs(d_a - d_l))) / 2
m = (x + d_p + (abs(x - d_p))) / 2
print(int(m))