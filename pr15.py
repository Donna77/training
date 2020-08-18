x = int(input())
a = x%10
b = x%100//10 
if b == 1:
	print(x, 'программистов')
elif a == 1:
	print(x, 'программист')
elif 2 <= a <= 4:
	print(x,'программиста')
else:
	print(x,'программистов')
