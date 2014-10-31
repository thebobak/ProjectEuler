#GLOBALS
FALSE = 0
TRUE = 1


#Create a 2D array with all possible products of 0-999

table = []

for x in range(1000):
	table.append([])
	for y in range(1000):
		table[x].append(x*y)


print table

def palindrome(n):
	
	word = str(n)
	length = len(word)
	start_index = 0
	end_index = length - 1
	flag = FALSE
	
	while (start_index < end_index):
		if (word[start_index] == word[end_index]):
			flag = TRUE
			start_index += 1
			end_index -= 1
		else:
			flag = FALSE
			break
	
	return flag
	

#Create list of palindromes
p_table = []
for x in range(1000):
	for y in range(1000):
		if (palindrome(table[x][y]) == TRUE):
			p_table.append(table[x][y])

p_table.sort()	
print p_table
			
print "The largest Palindrome is: "
print p_table[-1]