import matplotlib.pyplot as plt
import numpy as np
import random

# 1ST STEP 
Length = random.randint(50, 200)
Breath = float("{0:.2f}".format(Length / 6.5))
T = float("{0:.2f}".format(Breath / 6.5))
Cb = float("{0:.2f}".format(random.uniform(0.55, 0.85)))

#soru = input(f"What is the underwater volume and Buoyancy Force of the ship \n"
#	"which is {Length} meter length, {Breath} meter breath, {T} meters draft and Cb is {Cb}?")
UwVol = Length * Breath * T * Cb
#####################################
# 2ND STEP
# Waterlines and Frame Numbers lists
wl = np.array([0, 0.3, 1, 2, 3, 4, 5, 6]) #* T / 4
pn = np.array([0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5, 10]) #* Length / 10
waterlines = (wl)*(T/4) # Ödevde gösterildiği üzere değerleri düzenliyoruz. Liste şeklinde de yapabilirsiniz.
frame_numbers = (pn)*(Length/10)
#####################################
# Reading s60.txt, correcting and extracting lines
file = open("s60.txt")
# Waterlines plot preprocessing
listeler = []
for satir in file.readlines():
	line = (satir.replace("\n", "")).split(" ") # Satırlar arası virgül yok, onun yerine boşluk var. Ayrıca sonda \n var onu kaldırıyoruz.
	line = [float("{0:.4f}".format(float(value)*(Breath/2))) for value in line] # Aralardaki boşlukları split ederek otomatik olarak virgülle ayırmış oluyoruz. Ancak bu sefer de
	listeler.append(line) # aldığımız değerler string ifadeler oluyor. Float hale getirmek için üst satırdaki kodu yazıyoruz ve listelere ekliyoruz.
listeler_array = np.array(listeler) # ilk 6 satırı -1 ile çarpmak listeye göre daha kolay olduğu için array tipine  dönüştürüyoruz.
for i in range(6):
	listeler_array[i] = listeler_array[i] * -1

#Cross Section plot preprocessing
list_13 = [] # s60.txt dosyası her biri 8 değer içeren 13 satırdan oluşuyor cross section plot için her biri 13 değer içeren 8 satırlara dönüştürmeliyiz.
for i in range(8):
	for j in range(13):
		list_13.append(listeler[j][i]) # 35-38 satırları her biri 13 değer içeren 8 satırlık bir taslak yapıyor ancak satırları liste olarak belirtmiyor. 
liste_all = [list_13[x:x+13] for x in range(0, len(list_13), 13)] # Bunu yapabilmek için her 13 değerde bir, bir liste oluşturuyoruz.
# Şu anda liste_all da 8 tane her biri 13 değerlik listeler var. İstediğimizi yapmış olduk.
file.close()

with open(f"{Length}_{Breath}_{T}.txt", "w") as writing_file: # Yeni offset tablomuzu kaydetmek için 43-45 satırlarını yazıyoruz
	for line in listeler:
		writing_file.write(" ".join(map(str,line))+"\n")

##################################################################
# Plotting
fig = plt.figure()
axs1 = fig.add_subplot(2,1,1)
axs2 = fig.add_subplot(2,1,2)
for liste in listeler_array:
	axs1.plot(liste, waterlines)
for liste in liste_all:
	axs2.plot(frame_numbers, liste)
fig.savefig(f"{Length}_{Breath}_{T}.png")
plt.show()