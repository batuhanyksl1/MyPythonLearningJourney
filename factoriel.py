
#Faktöreyel hasaplayıcı
yildiz = "*"*30
v=10#int(input(f"{yildiz}\n\nHangi sayının faktöreyeli değerini öğrenmek istiyorsunuz?\n\n"))

x=1
y=1
while x <= v:
    print(f"{x-1} * {x} = {y}")
    x+=1
    y*=x
print(f"{v}! = {y}")