for i in range(3):
    sifre = input("Şifrenizi giriniz")
    if i == 2:#saymaya 0 dan başladığı için 2 yazıyorsun. 2 aslında dizideki 3. sayı
        print("şifreyi 3 kere yanlış girdiniz, 15 dakika bekleyin")
        break   
    elif len(sifre) in range (3,8):
        print("şifre girildi") 
        break
    elif not sifre:
        print("Bu alan boş bırakılamaz.")
    else: print("şifreniz 3-8 arasında olmalı")