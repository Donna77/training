x = int(input())
#if x%4 == 0:
#	if x%100 == 0:
#		if x//100 % 4 == 0:
#			print('Leap')
#		else:
#			print('Normal')
#	else:
#		print('Leap')
#else:
#	print('Normal')

if x%4 != 0 or x%100 == 0 and x%400 != 0:
	print('Normal')
else:
	print('Leap')