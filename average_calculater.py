# ekrana tam manası ile bir aritmetik ortalama makinesi yazacağız

#default gelecek başlık header
#açıklama
#sayı girişleri
#hesap sonucu
hm = "merhaba, ortalama hesaplayıcıma hoş geldiniz."
hs = "sizin için hazırladığım bu program ile gireceğiniz üç sayının aritmetik ortalmasını alabileceksiniz.\n\n"
print("\n\n\n"+hm.upper())
print(hs.capitalize())
n1 = float(input("ortalamaya katılacak sayı: "))
n2 = float(input("ortalamaya katılacak sayı: "))
n3= float(input("ortalamaya katılacak sayı: "))
r = (n1+n2+n3)/3
print("\n\nGirmiş olduğunuz sayıların ortalaması:", r,"\n")
