a = int(input())
b = int(input())
if a == b:
	print(a)
elif a > b:
	x = a
	while x%b != 0:
		x += a
	print(x)
elif b > a:
	x = b
	while x%a != 0:
		x += b
	print(x)
		