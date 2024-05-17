hesap=int(input("hesabı giriniz: "))
bahşiş = int(input("ne kadar bahşiş ödemek istiyorsunuz?)(yüzdelik olarak) :")
kisi=int(input("kaç kisi hesabı ödeyecek? :"))
tip=hesap*bahşiş/100
toplam=tip+hesap
ödeme=toplam/kişi
print("hesap ücreti: ", toplam)
print("bahşiş: ", tip)
print("kisi başı ödeme: ", ödeme)
#print(f"hesap ücreti{toplam}, bahşiş {tip}, kişi başı ödeme {ödeme})