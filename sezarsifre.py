k_alfabe = "abcçdefgğhıijklmnoöprsştuüvyzxwq +-*\\/)({}&%$#^'!abc"
b_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXWQ ABC"

menu = '''
[1]Şifrele
[2]Deşifre et!
[3]Çık!
'''

def menu1():
    print(menu)

menu1()

def main():
    while True:
        secim = input('İşleminiz: ')
        if secim == "1":
            cumle = input("Cumle: ")
            yeni_cumle = ""
            for i in cumle:
                if i in k_alfabe:
                    indeks = k_alfabe.index(i)
                    yeni_cumle += k_alfabe[indeks + 3]
                elif i in b_alfabe:
                    indeks = b_alfabe.index(i)
                    yeni_cumle += b_alfabe[indeks + 3]
                else:
                    print("Hatalı karakter girdisi!")
                    break
            print(yeni_cumle)
            menu1()
        elif secim == "2":
            cumle = input("Cumle: ")
            yeni_cumle = ""
            for i in cumle:
                if i in k_alfabe:
                    indeks = k_alfabe.index(i)
                    yeni_cumle += k_alfabe[indeks - 3]
                elif i in b_alfabe:
                    indeks = b_alfabe.index(i)
                    yeni_cumle += b_alfabe[indeks - 3]
                else:
                    print("Hatalı karakter girdisi!")
                    break
            print(yeni_cumle)
            menu1()
        elif secim == "3":
            break
        else:
            print("Hatalı seçim!")
            menu1()

main()
