import numpy as np
import matplotlib.pyplot as plt

# file = open("s60.txt")

# count=0
# for line in file.readlines():
# 	line = line.replace("\n","")
# 	line = line.split(" ")
# 	temp = []
# 	for value in line:
# 		if count > 47:
# 			value = float(value)
# 			temp.append(value)
# 			count += 1
# 		else:
# 			value = float(value) * -1
# 			temp.append(value)
# 			count += 1
# 	print(temp)

# 	#for value in line:
# 	#	print(value)
# file.close()


# file = open("s60.txt")

# temp = []
# count=0
# for line in file.readlines():
# 	line = (line.replace("\n","")).split(" ")
# 	line = [float(value) for value in line]
# 	temp.append(line)


# #for value in line:
# #	print(value)
# file.close()

file = open("s60.txt")

listeler = []
for line in file.readlines():
	line = (line.replace("\n", "")).split(" ")
	line = [float(value) for value in line]
	listeler.append(line)

list_13 = []
for i in range(8):
	for j in range(13):
		list_13.append(listeler[j][i])

chunks = [list_13[x:x+13] for x in range(0, len(list_13), 13)]
print(chunks)


# file.close()
# a = [1,2,3]
# a.clear()
# print(a)

# a = [1,2,3]
# print(len(a))