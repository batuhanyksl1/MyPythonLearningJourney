for i in range(3):
    sifre = input("Şifrenizi giriniz")
    if not sifre:
        print("Bu alan boş bırakılamaz.")
    elif len(sifre) in range (3,8):
        break
    elif i == 2:
        print("şifreyi 3 kere yanlış girdiniz, 15 dakika bekleyin")
    else: ("şifreniz 3-8 arasında olmalı")