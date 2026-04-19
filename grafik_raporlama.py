# ==========================================
# PROJE: Eğitim Verileri Görselleştirme
# YAZAR: Aslı Hüma
# AMAÇ: Sınav sonuçlarını grafiklerle analiz etmek.
# ==========================================

import matplotlib.pyplot as plt

# Örnek Veriler (Ders bazlı başarı oranları)
dersler = ['Python', 'SQL', 'Veri Analizi', 'İstatistik', 'Algoritma']
basari_oranlari = [85, 92, 78, 65, 88]

# 1. Bar Grafiği Oluşturma (Sütun Grafiği)
plt.figure(figsize=(10, 6))
plt.bar(dersler, basari_oranlari, color='skyblue')

# Grafiği Süsleme (Profesyonel görünüm için şart)
plt.title('Ders Bazlı Genel Başarı Oranları', fontsize=14)
plt.xlabel('Ders Adı', fontsize=12)
plt.ylabel('Başarı Yüzdesi (%)', fontsize=12)
plt.ylim(0, 100) # Y eksenini 0-100 arası sabitleyelim
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 2. Grafiği Kaydetme (GitHub'da resim olarak göstermek için kullanılabilir)
# plt.savefig('basari_grafigi.png')

print("Grafik başarıyla oluşturuldu. (Not: Bu kodun çıktısı bir görseldir.)")
plt.show()
