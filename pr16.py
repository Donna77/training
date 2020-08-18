abcdef = int(input())
a = abcdef//100000
b = abcdef%100000//10000
c = abcdef%10000//1000
d = abcdef%1000//100
e = abcdef%100//10
f = abcdef%10
if (a + b + c) == (d + f + e):
	print('Счастливый')
else:
	print('Обычный')
