import matplotlib.pyplot as plt
import numpy as np
import random

Length = 160 # random.randint(50, 200)
Breath = 24.62 # float("{0:.2f}".format((Length / 6.5)))
T = 3.79 # float("{0:.2f}".format((Breath / 6.5)))
Cb = 0.78 # float("{0:.2f}".format((random.uniform(0.55, 0.85))))


print(Length, Breath, T, Cb)

#soru = input(f"What is the underwater volume and Buoyancy Force of the ship \n"
#	"which is {Length} meter length, {Breath} meter breath, {T} meters draft and Cb is {Cb}?")

UwV = Length * Breath * T * Cb

###############
# 2nd Step
# Waterlines and Frame Numbers lists
w1 = np.array([0, 0.3, 1, 2, 3, 4, 5, 6]) #* T / 4
pn = np.array([0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5, 10]) #* Length / 10
waterlines = (w1)*(T/4)
frame_numbers = (pn)*(Length/10)

# for i in w1:
# 	i *= T / 4
# 	waterlines.append(i)
# for j in pn:
# 	j *= Length / 10
# 	frame_numbers.append(j)
#####################################
# Reading s60.txt, correcting and extracting lines 
# for Waterlines and Cross Section plots
file = open("s60.txt")

listeler = []
for satir in file.readlines():
	line = (satir.replace("\n", "")).split(" ")
	line = [float("{0:.4f}".format(float(value)*(Breath/2))) for value in line]
	print(line)
	listeler.append(line)

listeler_array = np.array(listeler)
for i in range(6,13):
	listeler_array[i] = listeler_array[i] * -1
listeler_array = listeler_array

list_13 = []
for i in range(8):
	for j in range(13):
		list_13.append(listeler[j][i])
liste_all = [list_13[x:x+13] for x in range(0, len(list_13), 13)]

# for i in list_all:
# 	plt.plot(frame_numbers, i)

# Plotting
# for liste in listeler_array:
# 	plt.plot(liste, waterlines)

file.close()
#for i in listeler:
#	if


# lines = ['line1', 'line2']
# with open('filename.txt', 'w') as f:
#     f.write('\n'.join(lines))
#writing_file = open(f"{str(Length)}_{str(Breath)}_{str(T)}.txt", "w")
# for i in range(13):
# 	for j in range(8):
# 		value = listeler[i][j]
# 	print(value,"/n")
#writing_file.close()

# file2 = open(f"{Length}_{Breath}_{T}", "w")
# plt.show()
#####################################
# PLOTTING
# for liste in listeler:
# 	plt.plot(liste, waterlines)
# plt.show() 

# file = open("s60.txt", "r")
# for a in file.readlines():
# 	print(a)


# fig, axs = plt.subplots(2) # figsize=(8,7)
# fig.suptitle('Graphs')
# # fig.figsize(10,7) # doesnt work

# # Waterlines Plot
# for liste in listeler_array: 	
# 	axs[0].plot(liste, waterlines)
# # Cross Section Plot
# for liste in liste_all:
# 	axs[1].plot(frame_numbers, liste)
# plt.show()
# fig.savefig(f"{Length}_{Breath}_{T}.png")

fig = plt.figure()
axs1 = fig.add_subplot(2,1,1)
axs2 = fig.add_subplot(2,1,2)
for liste in listeler_array:
	axs1.plot(liste, waterlines)
for liste in liste_all:
	axs2.plot(frame_numbers, liste)
fig.savefig(f"{Length}_{Breath}_{T}.png")