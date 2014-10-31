#GLOBALS
FALSE = 0
TRUE = 1

sumofsquares = 0
squareofsums = 0

for i in range(101):
	sumofsquares += (i*i)

print sumofsquares


for i in range(101):
	squareofsums += i
	
print squareofsums
	
totalsquares = squareofsums * squareofsums


print (totalsquares - sumofsquares)