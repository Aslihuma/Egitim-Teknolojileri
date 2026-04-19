-- ==========================================
-- PROJE: Eğitim Kurumu SQL Raporlama Sorguları
-- YAZAR: Aslı Hüma
-- AMAÇ: Veri tabanından devamsızlık ve başarı raporları çekmek.
-- ==========================================

-- 1. En Yüksek Devamsızlık Yapan İlk 10 Öğrenciyi Listele
-- Bu sorgu, rehberlik servisinin hangi öğrencilerle görüşmesi gerektiğini belirler.
SELECT ad_soyad, devamsizlik_gun_sayisi, sinif
FROM Ogrenciler
WHERE devamsizlik_gun_sayisi > 5
ORDER BY devamsizlik_gun_sayisi DESC
LIMIT 10;

-- 2. Sınıf Bazında Not Ortalamalarını Hesapla
-- Hangi sınıfların daha başarılı olduğunu analiz etmek için kullanılır.
SELECT sinif, AVG(final_notu) AS sinif_ortalamasi
FROM Sinavlar
GROUP BY sinif
HAVING sinif_ortalamasi < 60; -- Ortalaması 60'ın altındaki kritik sınıflar

-- 3. Etkinliklere Katılan ve Katılmayan Öğrenci Sayısı
-- Sosyal katılımın analizi için.
SELECT 
    CASE 
        WHEN etkinlik_sayisi > 0 THEN 'Aktif Öğrenci'
        ELSE 'Pasif Öğrenci'
    END AS katilim_durumu,
    COUNT(*) AS ogrenci_sayisi
FROM Ogrenci_Sosyal_Tablo
GROUP BY katilim_durumu;
