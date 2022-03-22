from tkinter import *
import time


bilgiler = ("demo","demo123",'18')
denemeHakki = 3
zaman = 0
def girisYap():
    global denemeHakki, zaman
    
    if denemeHakki <= 0:
        if time.time()-zaman >= 5:
            denemeHakki = 3
        else:
            sonuc.config(text = u"Lutfen 5 saniye bekleyiniz.")
            return False
    
    kAdi = isim.get()
    parola = sifre.get()
    yas = age.get()
    print (kAdi, " - ", parola, " - ", yas)
    print ("Kontrol ediliyor ...")
    if kAdi == bilgiler[0] and parola == bilgiler[1] and yas == bilgiler[2]:
        print ("Bilgiler dogru!")
        sonuc.config(text = u"Oturum acma islemi basarili.")
        ekraniTemizle()
        veri = (f"""Isim: {kAdi}
Parola: {parola}
Yas: {yas}""")
        file_created = open('C:\\Users\\user\Desktop\\Devoloper\\python\\lecture\\projects\\kayit_islemi\\veri_tabani.txt', 'w')
        file_created.write(veri)
        file_created.close()
        #time.sleep(3)
        #exit()
        
    else:
        print ("Bilgiler yanlis!")
        denemeHakki -= 1
        if denemeHakki == 0:
            zaman = time.time()
        sonuc.config(text = u"Bilgiler yanlis. Kalan deneme hakki: %d" %denemeHakki)
        
def ekraniTemizle():
    karsilama.config(text = u"Hosgeldin, Demo!")
    isimSor.destroy()
    isim.destroy()
    sifreSor.destroy()
    sifre.destroy()
    age.destroy()
    buton.destroy()


pencere = Tk()

pencere.title(u"X.com.tr - Python Project")
pencere.geometry("290x200+100+100")

karsilama = Label(pencere)
karsilama.config(text = u"Hosgeldiniz, lutfen giris yapiniz.")
karsilama.pack()

isimSor = Label(pencere)
isimSor.config(text = u"Kullanici Ismi:")
isimSor.pack()

isim = Entry(pencere)
isim.pack()

sifreSor = Label(pencere)
sifreSor.config(text= u"Sifreniz: ")
sifreSor.pack()

sifre = Entry(pencere)
sifre.pack()

agesor = Label(pencere)
agesor.config(text = u"Yas: ")
agesor.pack()

age = Entry(pencere)
age.pack()

buton = Button(pencere)
buton.config(text = u"Giris yap!", command = girisYap)
buton.pack()

sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack()

mainloop ()
