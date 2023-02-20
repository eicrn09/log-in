username=input('Bir kullanici adi belirleyin: ')
password=input("Bir sifre belirleyin: ")

noktasayisi=int(1)
while noktasayisi<=1054:
    print('.')
    noktasayisi+=1

a=input('kullanici adiniz: ')
b=input('sifreniz: ')
if (username==a):
    if (password== b):
        print("Hos Geldiniz")
    else:
         print(" Sifre Yanlis")
else:
    print('Kullanici Adi Yanlis')