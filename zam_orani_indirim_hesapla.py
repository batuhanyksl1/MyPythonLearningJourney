"""öncelikle burada zam mı indirim mi istediğini öğreneceğiz
    ZAM
    değişkenler:    tutar
                    zam  oranı
                    zamlı tutar
                    zam miktarı
    İNDİRİM
    değişkenler:    tutar
                    indirim oranı
                    indirimli tutar
                    indirim mikterı
    """
#variables
print("*" * 150,"\n\nZam ve İndirim hesaplayıcımıza hoşgeldiniz.\n\n")
ara = "-"*30
r1 = "Zam"
r2 = "İndirim"
sr1 = "İndirim tutarı hesaplama"
sr2 = "İndirimli tutardan ilk tutar hesaplama"
sr3 = "Zam tutarı ve zamlı tutar hesapla"
sr4 = "Zamlı tutaradan ilk tutar hesapla"
test = "f"
req = input(f"Hesaplama yapmak istediğiniz konu\n\n{r1} ile mi ilgili?,\n{r2} ile mi ilgili? \n\nbelirtiniz: ")
print(ara)
if r1.lower() in req.lower():
    sr = input(f"\n\nYapmak istediğiniz işlem\n\n{sr3} mı?\n{sr4} mı?\n\n->")
    if sr3.lower() in sr.lower():
        amt = float(input(f"\n{r1} öncesi tutarı giriniz: "))
        rate = int(input(f"{r1} oranını giriniz: "))
        new_amt = amt * ( 1 + rate / 100)
        dif = new_amt - amt
        print(f"\nZamlı tutarınız: {new_amt:.2f} TL\nZam tutarı: {dif:.2f} TL\n")
    else:
        #sr4.lower() in sr.lower()
        new_amt = float(input(f"\n{r1}lı tutarı giriniz: "))
        rate = int(input(f"{r1} oranını giriniz: "))
        amt = (new_amt * 100)/ (100 + rate)
        #amt * ( 1 + rate / 1
        #dif = new_amt - amt
        print(f"\nZamlı tutarınız: {amt:.2f} TL\n")
else:
    print

#print(new_amt, dif)