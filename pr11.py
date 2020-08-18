a = int(input())
#if ((-15 < a) and (a <= 12)) or ((14 < a) and (a < 17)) or (a >= 19):
if (-15 < a <= 12) or (14 < a < 17) or (a >= 19):
	print('True')
else:
	print('False')