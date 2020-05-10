import sys
import time

strings = []
sResult = ""
tResult = ""

print ("\nInput Sequences\n----------------------------------------------")
"""for i in sys.argv[1:]:
	file = open(i, 'r')
	contents = file.read()
	file.close()
	print(contents)
	strings.append(contents)
"""
strings = ['GGAAGGGGCGATCGGAGGGC', 'GGTAAGGGGCCTGATCGAAGGGCAA']

str1 = strings[0]
str2 = strings[1]

print(str1)
print(str2)

startTime = time.time()
rows = len(str1) + 1
columns = len(str2) + 1

matrix = [[0 for x in range(rows)] for x in range(columns)]
auxilaryMatrix = [[0 for x in range(rows)] for x in range(columns)]

for col in range(columns):
	matrix[col][0] = col
for row in range(rows):
	matrix[0][row] = row

for i in range(1, columns):
	for j in range(1, rows):
		if str1[j-1] == str2[i-1]:
			matrix[i][j] = matrix[i-1][j-1]
			auxilaryMatrix[i][j] = 0

		else:
			matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1)
			if matrix[i][j] == matrix[i-1][j]+1:
				auxilaryMatrix[i][j] = 1
			elif matrix[i][j] == matrix[i][j-1]+1:
				auxilaryMatrix[i][j] = 2
			else:
				auxilaryMatrix[i][j] = 0
editDist = matrix[-1][-1]


for i in range(columns-1, 0, -1):
	for j in range(rows-1, 0, -1):
		if auxilaryMatrix[i][j] == 0:
			sResult += str(str1[j-1])
			tResult += str(str2[i-1])
			i -= 1
			j -=1
		elif auxilaryMatrix[i][j] == 1:
			sResult += "-"
			tResult += str(str2[i-1])
			i -=1
		elif auxilaryMatrix[i][j] == 2:
			sResult += str1[j-1]
			tResult += "-"
			j-=1
			

print("----------------------------------------------\n Aligned Sequences")
print(sResult[columns::-1])
print(tResult[columns::-1])

elapsedTime = time.time() - startTime
print("----------------------------------------------\n")
print("The mininimum edit distance is", editDist)
print("Completed in ", elapsedTime, "Seconds")