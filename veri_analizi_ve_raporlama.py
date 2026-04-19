# ==========================================
# PROJE: Eğitim Teknolojileri Veri Analizi
# YAZAR: Aslı Hüma MUTLU
# AMAÇ: Öğrenci performans verilerini analiz etmek ve otomatik rapor oluşturmak.
# ==========================================

import pandas as pd  # Veri analizi için en temel kütüphaneyi içeri aktarıyoruz

# 1. ÖRNEK VERİ SETİ OLUŞTURMA
# Gerçek projelerde bu veriler bir Excel'den (.xlsx) veya SQL veri tabanından gelir.
data = {
    'Ogrenci_ID': [101, 102, 103, 104, 105],
    'Ad_Soyad': ['Ayşe Yılmaz', 'Mehmet Demir', 'Fatma Kaya', 'Ali Can', 'Zeynep Ak'],
    'Sinav_Notu': [85, 42, 90, 38, 75],
    'Devamsizlik': [2, 12, 0, 15, 5],
    'Katildigi_Etkinlik_Sayisi': [5, 1, 8, 0, 4]
}

# Verileri Pandas "DataFrame" yapısına dönüştürüyoruz (Analiz için standart yapı)
df = pd.DataFrame(data)

# 2. VERİ ANALİZİ FONKSİYONU
def analiz_yap(dataframe):
    print("--- ÖĞRENCİ ANALİZ RAPORU BAŞLATILIYOR ---\n")
    
    # Başarı Durumu Belirleme: Notu 50'den büyükse 'Geçti', küçükse 'Kaldı'
    dataframe['Durum'] = dataframe['Sinav_Notu'].apply(lambda x: 'BAŞARILI' if x >= 50 else 'RİSKLİ')
    
    # Kritik Öğrenci Filtreleme: Hem notu düşük hem devamsızlığı yüksek olanlar
    riskli_ogrenciler = dataframe[(dataframe['Sinav_Notu'] < 50) & (dataframe['Devamsizlik'] > 10)]
    
    return dataframe, riskli_ogrenciler

# 3. SONUÇLARI HESAPLA VE EKRANA YAZDIR
analiz_sonucu, riskli_liste = analiz_yap(df)

print("Tüm Liste ve Durum Analizi:")
print(analiz_sonucu[['Ad_Soyad', 'Sinav_Notu', 'Durum']])

print("\n--- DİKKAT: Takip Edilmesi Gereken Riskli Öğrenciler ---")
if not riskli_liste.empty:
    print(riskli_liste[['Ad_Soyad', 'Devamsizlik', 'Sinav_Notu']])
else:
    print("Şu an kritik durumda olan öğrenci bulunmamaktadır.")

# 4. İSTATİSTİKSEL ÖZET (Analistin gücünü gösterir)
ortalama_not = df['Sinav_Notu'].mean()  # Sınıfın not ortalamasını hesaplar
print(f"\nSınıf Genel Not Ortalaması: {ortalama_not}")

# 5. DIŞARI AKTARMA (Opsiyonel)
# analiz_sonucu.to_excel("ogrenci_raporu.xlsx", index=False) # Analizi Excel olarak kaydeder
