x = int(input())
a = x%10
b = x%100//10 
s = 'программист'
if b == 1:
	p ='ов'
elif a == 1:
	p = ''
elif 2 <= a <= 4:
	p = 'а'
else:
	p = 'ов'
print(x,' ',s,p, sep='')