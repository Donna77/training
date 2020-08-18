x = int(input())
if x%4 != 0 or x%100 ==0 and x%400 != 0:
	print('Обычный')
else:
 	print('Високосный')