# 📺 Kişisel Dizi İzleme ve Analiz Paneli

## Problem Tanımı
Bireysel izleyicilerin takip ettikleri çok bölümlü dizileri, izleme alışkanlıklarını, türe göre harcadıkları zamanı ve verdikleri puanları manuel olarak takip etmesinin karmaşık ve zor olması.

## Hedef Kullanıcı
Kendi izleme istatistiklerini analiz etmek, veriye dayalı kararlar görmek ve bu doğrultuda kişiselleştirilmiş dizi önerileri almak isteyen bireysel izleyiciler.

## Çözümün Kısa Açıklaması
Kullanıcıların izleme verilerini yükleyerek grafikler ve metrikler eşliğinde geriye dönük analiz yapabildiği, aynı zamanda içeride çalışan yerel yapay zekâ mantığı (Kural Tabanlı AI) sayesinde favori tarzlarına göre nokta atışı yeni dizi önerileri alabildiği etkileşimli bir web paneli.

## Kullanılan Teknolojiler
* **Python:** Temel programlama mantığı.
* **Pandas:** İki farklı veri tablosunu birleştirme ve metrik hesabı.
* **Streamlit:** Etkileşimli web arayüzü ve filtreleme mekanizması.
* **Matplotlib / Streamlit Charts:** Veri görselleştirme ve grafik üretimi.

## Sistem Mimarisi ve İş Akışı
1. `diziler.csv` ve `puanlar.csv` dosyaları Pandas ile 'Dizi Adı' ortak sütunu üzerinden birleştirilir.
2. Toplam dizi, toplam bölüm, ortalama puan, en yüksek puan ve favori tür metrikleri hesaplanır.
3. Kullanıcı arayüzde tür filtresi seçtiğinde veriler dinamik olarak filtrelenir ve grafik güncellenir.
4. "Verilerimi Analiz Et ve Dizi Öner!" butonuna basıldığında yerel yapay zekâ algoritması çalışarak kullanıcıya akıllı kararlar ve öneriler sunar.

## Kurulum Adımları
Projeti yerelde çalıştırmak için aşağıdaki komutları terminalinizde sırayla çalıştırın:
```bash
# Gerekli kütüphanelerin kurulumu
pip install pandas streamlit matplotlib

# Uygulamanın başlatılması
streamlit run app.py


## Tanıtım Videosu
[https://drive.google.com/file/d/1ft2D_V-1v7imtBh8uvBhDBSKS_AQwL39/view?usp=sharing]
