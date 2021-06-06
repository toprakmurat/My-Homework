from tkinter import *
from sympy import *
import re

class MyWindow:
    """
    Bu modül Murat Toprak'ın Matematik proje ödevi için yazılmıştır.
    
    Amacı kullanıcıların fonksiyonlar ile ilgili bazı işlemleri daha kolay
    yapmasını sağlamaktır.

    tersini_al metodu bir basit bir f() fonksiyonun tersini almak için yazılmıştır.
    Örnek Girdi: f(x) = x+2 ise girdi olarak x+2 yazmanız gerekmektedir.
    Örnek Çıktı: {x: y-2}
    
    coz_basit metodu bir basit fonksiyonun x yerine yazılması gereken sayının
    kullanıcı tarafından verilmesiyle fonksiyonu çözer.
    Örnek Girdi: f(x) = 37*x + 13, f(9)
    Örnek Çıktı: 346

    coz_merdiven metodu ise merdiven tipli çözülmesi gereken sorular için yazılmıştır.
    Kullanıcının Soru tarafından sağlanan Fonksiyon, Sorulan ve Bilgi değerlerini girmesi
    gerekmektedir.
    Örnek Girdi: f(x) = f(x-2) + x, f(22), f(0) = 1
    Örnek Çıktı: 133
    
    fonksiyon: string, her metod için gereken parametre (fonksiyon)
    sorulan: string veya int, coz_merdiven ve coz_basit için gerekli olan sorulan fonksiyondur. 
    bilgi: string, coz_merdiven için gerekli olan soru tarafından verilen bilgi
    
    ENGLISH

    fonksiyon : string, the function to do operations with
    sorulan : string or int, the wanted function
    bilgi : string, the information about the function which question provides

    """
    def __init__(self, win):
        self.lbl1=Label(win, text='Fonksiyon')
        self.lbl2=Label(win, text='Sorulan')
        self.lbl3=Label(win, text='Bilgi')
        self.lbl4=Label(win, text='Sonuc')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.btn1=Button(win, text='Tersini Al')
        self.btn2=Button(win, text='Basit Fonksiyon Coz')
        self.btn3=Button(win, text='Merdiven Fonksiyon Coz')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.b1=Button(win, text='Tersini Al', command=self.tersini_al)
        self.b2=Button(win, text='Basit Fonksiyon Coz')
        self.b2.bind('<Button-1>', self.coz_basit)
        self.b3=Button(win, text='Merdiven Fonksiyon Coz')
        self.b3.bind('<Button-1>', self.coz_merdiven)
        self.b1.place(x=50, y=200)
        self.b2.place(x=150, y=200)
        self.b3.place(x=300, y=200)
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)
    
    def tersini_al(self):
        self.t4.delete(0, 'end')
        fonksiyon = self.t1.get()
        eq = fonksiyon + "  = y"
        sympy_eq = sympify("Eq(" + eq.replace("=", ",") + ")")
        cozum = solve(sympy_eq)
        
        return self.t4.insert(END, cozum[0])
        # return cozum[0]

    def coz_basit(self, event):
        fonksiyon = self.t1.get()
        sorulan = self.t2.get()
        
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
        
        return self.t4.insert(END, sonuc)

    def coz_merdiven(self, event):
        fonksiyon = self.t1.get()
        sorulan = self.t2.get()
        bilgi = self.t3.get()

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

        return self.t4.insert(END, sonuc)

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("500x350+10+10")
window.mainloop()


# RESULT KARŞISINDAKI KUTUCUĞU YAZILABILIR YAPMA