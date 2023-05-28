import random

# Adayların oy sayıları
aday1_oy = 0
aday2_oy = 0
gecersiz_oy =0

# Seçmen sayısı
secmen_sayisi = 1000000

# Adayların kazanma yüzdeleri
aday1_yuzde = 55.7
aday2_yuzde = 43.0
gecersiz_yuzde = 0.3



# Seçim simülasyonu
for _ in range(secmen_sayisi):
    # Rastgele bir sayı seçme (0-99 arası)
    rastgele_sayi = random.randint(0, 99)
    
    # Geçersiz oy
    if rastgele_sayi < gecersiz_yuzde:
        gecersiz_oy += 1
    # Aday1'e oy verme
    elif rastgele_sayi < aday1_yuzde + gecersiz_yuzde:
        aday1_oy += 1
    # Aday2'ye oy verme
    else:
        aday2_oy += 1

# Sonuçları yüzdelere dönüştürme
aday1_yuzde = (aday1_oy / secmen_sayisi) * 100
aday2_yuzde = (aday2_oy / secmen_sayisi) * 100
gecersiz_yuzde = (gecersiz_oy / secmen_sayisi) * 100

# Sonuçları yazdırma yüzde
print("Aday 1 Oy Yüzdesi: {:.2f}%".format(aday1_yuzde))
print("Aday 2 Oy Yüzdesi: {:.2f}%".format(aday2_yuzde))
print("Geçersiz Oy Yüzdesi: {:.2f}%".format(gecersiz_yuzde))

# Sonuçları yazdırma
print("Aday 1 Oy Sayısı:", aday1_oy)
print("Aday 2 Oy Sayısı:", aday2_oy)
print("Geçersiz Oy Sayısı:", gecersiz_oy)
