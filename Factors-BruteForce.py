#GLOBALS
FALSE = 0
TRUE = 1

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Brute Force method with outputs


x = 20
flag = FALSE
checksum = 0
while x:
	checksum = 0
	print "Now Testing:  "
	print x
	
	
	for i in range(1,21):  #divide x by every number, 1-20
		if (x % i == 0):
			checksum += 1  #tally up whether it divides evenly

			
		
	if (checksum == 20):
		break
	else:
		x += 20
		print checksum

print "The current value of x is:  "
print x