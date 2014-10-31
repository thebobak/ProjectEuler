from math import sqrt

#GLOBALS
FALSE = 0
TRUE = 1

#List and count of all prime numbers
primes = [2,3,5,7,11,13,17,19,29,31]
count = len(primes)
primes_to_seek = 15
x = 32

while (count < primes_to_seek):
	print "now testing %s" % x
	xs = str(x)
	lastdigit = xs[-1]
	xroot = sqrt(x)
	
	#Check the last digit of the number
	#if last digit is 0,2,4,5,6,8, move on to next number
	if (lastdigit == "0" or lastdigit == "2" or lastdigit == "4" or lastdigit == "5" or lastdigit == "6" or lastdigit == "8"):
		print "%s is NOT prime (last digit)" % x
		x+=1
			
	# check if sqrt is an INT, skip number if it is
	elif (isinstance(xroot, int) == TRUE):
		print "%s is NOT prime (has root)" % x
		x+=1
		
	else:
		flag = TRUE
		i = 2
		while (i < int(xroot)):
			if (x%i == 0):
				flag = FALSE
			i+=1
		
		if (flag == TRUE):
			primes.append(x)
			count = len(primes)
			print "Prime Found: %s" % x
			x+=1
		elif (flag == FALSE):
			print "%s is NOT prime (division test)" % x
			x+=1
		
				


print "The list of Primes is:"
print primes
print "The End"
