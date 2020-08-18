import sys
X = int(sys.argv[1])
H = int(sys.argv[2])
M = int(sys.argv[3])
y = X + H*60 + M
print(y//60)
print(y%60)
