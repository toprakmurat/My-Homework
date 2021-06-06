from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from sympy import *
import re

class MyWindow:
	def __init__(self, win):
		self.t1 = StringVar()
		self.t2 = StringVar()
		self.t3 = StringVar()
		self.t4 = StringVar()

		self.frame1 = Frame(win, height=750, width=1330, bg="#D3D3D3")
		self.frame1.place(x=0, y=0)
		self.background = Label(self.frame1, image=render)
		self.background.place(x=0, y=0)

		self.e1 = Entry(self.frame1, font=("arial", 15), bd=4, textvariable=self.t1, width=25)
		self.e1.place(x=750, y=125)
		self.l1 = Label(self.frame1, text="Fonksiyon", font=("arial", 18, "normal"), bg="#121212", fg="#ffffff", width=10)
		self.l1.place(x=600, y=125)
		self.b1 = Button(self.frame1, image=render_image1, command=self.tersini_al)
		self.b1.place(x=750, y=175)

		self.e2 = Entry(self.frame1, font=("arial", 15), bd=4, textvariable=self.t2, width=25)
		self.e2.place(x=750, y=275)
		self.l2 = Label(self.frame1, text="Sorulan", font=("arial", 18, "normal"), bg="#121212", fg="#ffffff", width=10)
		self.l2.place(x=600, y=275)
		self.b2 = Button(self.frame1, image=render_image2)
		self.b2.bind('<Button-1>', self.coz_basit)
		self.b2.place(x=767, y=325)

		self.e3 = Entry(self.frame1, font=("arial", 15), bd=4, textvariable=self.t3, width=25)
		self.e3.place(x=750, y=425)
		self.l3 = Label(self.frame1, text="Ek Bilgi", font=("arial", 18, "normal"), bg="#121212", fg="#ffffff", width=10)
		self.l3.place(x=600, y=425)
		self.b3 = Button(self.frame1, image=render_image3)
		self.b3.bind('<Button-1>', self.coz_merdiven)
		self.b3.place(x=750, y=475)

		#####################################################################
		# Ogrenci Bilgilerim ve diger bilgiler
		self.ad_soyad = Label(self.frame1, text="Murat Toprak", font=("arial", 20, "normal"), bg="#121212", fg="#ffffff", width=10)
		self.ad_soyad.place(x=125, y=75)
		self.sınıf_no = Label(self.frame1, text="10-C / 176", font=("arial", 20, "normal"), bg="#121212", fg="#ffffff", width=10)
		self.sınıf_no.place(x=120, y=110)
		self.ogretmen = Label(self.frame1, text="Öğretmen: Mehmetali Harman", font=("arial", 20, "normal"), bg="#121212", fg="#ffffff")
		self.ogretmen.place(x=50, y=560)
		self.dipnot = Label(self.frame1, text="Umarım beğenirsiniz", font=("arial", 20, "normal"), bg="#121212", fg="#ffffff")
		self.dipnot.place(x=100, y=610)
		#####################################################################

		# Cevap Kısmı
		#cevap = Label(frame1, image=render_cevap)
		#cevap.place(x=620, y=601)
		self.cevap = Label(self.frame1, text="Cevap", font=("arial", 20, "normal"), bg="#121212", fg="#ffffff")
		self.cevap.place(x=635, y=595)
		self.entry = Entry(self.frame1, font=("arial", 15), bd=4, textvariable=self.t4, width=25)
		self.entry.place(x=750, y=600)

	def tersini_al(self):
		fonksiyon = self.e1.get()
		eq = fonksiyon + "  = y"
		sympy_eq = sympify("Eq(" + eq.replace("=", ",") + ")")
		cozum = solve(sympy_eq)

		return self.t4.set(cozum)
		# return cozum[0]

	def coz_basit(self, event):
		fonksiyon = self.e1.get()
		sorulan = self.e2.get()

		x = Symbol("x")
		ifade_to_parse = fonksiyon[fonksiyon.find("(")+1:fonksiyon.find(")")]  #i.e f(2*x+1)=x+5, result=2*x+1
		ifade = parse_expr(ifade_to_parse)

		islem_to_parse = fonksiyon.split("=")[1]
		islem = parse_expr(islem_to_parse)

		pattern = r"\d+"
		sorulan = int(re.findall(pattern, sorulan)[0]) 
		# sorulan = parse_expr(sorulan)
		# simplified = sympify(f"Eq({ifade}, {deger})")
		x_degeri = solve(Eq(ifade, sorulan))[0]
		sonuc = islem.subs(x, x_degeri)

		return self.t4.set(sonuc)

	def coz_merdiven(self, event):
		fonksiyon = self.e1.get()
		sorulan = self.e2.get()
		bilgi = self.e3.get()

		fonksiyon = fonksiyon.split("=")
		ilk_kısım, ikinci_kısım = sympify(fonksiyon[0]), sympify(fonksiyon[1])
		fonksiyon = ilk_kısım + (-1 * ikinci_kısım)

		bilgi = bilgi.split("=")
		bilgi0, bilgi1 = sympify(bilgi[0]), sympify(bilgi[1])
		bilgi = {bilgi0: bilgi1}

		pattern = r"\d+"
		sorulan = sympify(re.findall(pattern, sorulan)[0]) # f(25) = 25, just "25" is also 25

		formula = rsolve(fonksiyon, sympify("f(x)"), bilgi)
		sonuc = formula.subs(sympify("x"), sorulan)

		return self.t4.set(sonuc)

window = Tk()

######################################################
# gereken resimleri yükle
load = Image.open("wallpaper.JPG")
render = ImageTk.PhotoImage(load)

image1_load = Image.open("fonksiyonun tersini al.JPG")
render_image1 = ImageTk.PhotoImage(image1_load)

image2_load = Image.open("basit fonksiyon çöz.JPG")
render_image2 = ImageTk.PhotoImage(image2_load)

image3_load = Image.open("merdiven fonksiyon çöz.JPG")
render_image3 = ImageTk.PhotoImage(image3_load)
######################################################

mywin = MyWindow(window)
window.title("Matematik Proje Ödevi")
window.geometry("1330x750")
window.mainloop()