a = float(input())
b = float(input())
c = input()
if (c in ('/', 'div', 'mod')) and (b == 0):
	print('Division by zero')
elif c == '+':
	print (a + b)
elif c == '-':
	print (a - b)
elif c == '/':
	print (a/b)
elif c == '*':
	print (a*b)
elif c == 'mod':
	print (a%b)
elif c == 'pow':
	print (a**b)
elif c == 'div':
	print (a//b)
else:
	print('Invalid input')