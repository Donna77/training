a = int(input())
b = int(input())
s = 0
j = 0
if a%3 != 0:
	a += 3 - a%3
for i in range(a, b+1, 3):
	s += i
	j += 1
print(s/j)