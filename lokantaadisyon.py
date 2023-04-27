import os
masalar = dict()
for i in range(10):
    masalar[i] = 0

def hesapEkle():
    masaNo = int(input("Masa No:"))
    gecerli = masalar[masaNo]
    eklenecek = float(input("Eklenecek ücret: "))
    toplam = gecerli + eklenecek
    masalar[masaNo] = toplam

def hesapSil():
    masaNo = int(input("Masa No:"))
    gecerli = masalar[masaNo]
    silinecek = float(input("Silinecek ücret: "))
    toplam = gecerli - silinecek
    masalar[masaNo] = toplam
def hesapKontrol(dosya_adi):
    veriler= list()
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya= open(dosya_adi,"w")
        dosya.close()
        flag = False
    if flag:
       for i in enumerate(veriler):
           if i[1]:
            masalar[i[0]] = float(i[1])
           else:
               break
    else:
        pass
def kayitGuncelle():
    dosya = open("kayıtlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()


def main():
    hesapKontrol("kayıtlar.txt")
    while True:
        os.system("cls")
        print("""
        1 masaları görüntüle
        2 hesap ekle
        3 hesap sil
        4 çıkış
        """)

        secim = input("işleminiz: ")
        if secim == "1":
            for i in range(10):
                print("Masa {} için hesap: {}".format(i, masalar[i]))

        elif secim == "2":
            hesapEkle()
            print("işlem tamam")
            input()

        elif secim == "3":
            hesapSil()
            print("işlem tamam.")
            input()
        else:
            print("xsscsc")

main()