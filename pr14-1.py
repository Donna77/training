a = int(input())
b = int(input())
c = int(input())

#if a >= b and a >= c and c >= b:
#	print(a,b,c)
#elif a >= b and a >= c and b >= c:
#	print(a,c,b)
#elif b >= a and b >= c and c >= a:
#	print(b,a,c)
#elif b >= a and b >= c and a >= c:
#	print(b,c,a)
#elif c >= a and c >= b and b >= a:
#	print(c,a,b)
#elif c >= a and c >= b and a >= b:
#	print(c,b,a)

if b <= a >= c:
	if c >= b: print(a,b,c)
	else:      print(a,c,b)
elif a <= b >= c:
	if c >= a: print(b,a,c)
	else:      print(b,c,a)
elif a <= c >= b:
	if b >= a: print(c,a,b)
	else:      print(c,b,a)