# PROJE ÖNERİSİ

**Seçilen Görev Numarası:** SEÇENEK 5 - Akıllı Veri Ürünü, Gösterge Paneli veya Çok Modlu Uygulama

**Ürünün Adı:** Kişisel Dizi İzleme ve Analiz Paneli

**Çözülecek Problem:** Bireysel izleyicilerin takip ettikleri dizileri (özellikle çok bölümlü Çin dramaları gibi içerikleri), hangi türlere daha çok vakit harcadıklarını ve verdikleri puanları manuel olarak takip etmesinin karmaşık ve zor olması.

**Hedef Kullanıcı:** Kendi izleme alışkanlıklarını analiz etmek, istatistiklerini görmek ve bu verilere dayanarak yeni içerik keşfetmek isteyen bireysel izleyiciler.

**Kullanılacak Veri veya Bilgi Kaynakları:**
- `diziler.csv`: Dizi adı, türü (Tarihi, Romantik, Fantastik vb.) ve toplam bölüm sayısını içeren tablo.
- `puanlar.csv`: Dizi adı, izlenen bölüm sayısı ve kullanıcı değerlendirme puanını (1-10) içeren tablo.

**Kullanılması Planlanan Teknolojiler:**
- **Python:** Veri işleme ve temel mantık.
- **Pandas:** İki farklı veri tablosunu birleştirme, temizleme ve analiz metriklerini hesaplama.
- **Streamlit:** Kullanıcı arayüzü (dashboard) oluşturma ve filtreleme özellikleri.
- **Matplotlib:** İzleme istatistiklerinin görselleştirilmesi.
- **LLM API:** Kullanıcının yüksek puan verdiği içeriklere göre doğal dilde yeni dizi önerileri sunmak için.

**Beklenen Ürün Çıktısı:**
Kullanıcının türlere göre filtreleme yapabildiği, izleme istatistiklerini (toplam izlenen bölüm, en yüksek puanlı tür vb.) grafiklerle görebildiği ve bu istatistiklere dayanarak yapay zekadan yeni içerik önerileri alabildiği etkileşimli bir web paneli. Projede makine öğrenmesi ve tahmine dayalı modelleme yerine, tamamen veri analizi ve görsel yorumlama odaklı bir yaklaşım benimsenecektir.

**Ürünün Diğer Çalışmalardan Ayrılan Yönü:**
Genel geçer önerme sistemlerinin aksine, tamamen kullanıcının kendi kişisel izleme verisi üzerinden çalışan, hem geriye dönük veri analizi (dashboard) sunan hem de LLM entegrasyonu ile ileriye dönük kişiselleştirilmiş bir asistan işlevi gören kompakt bir veri ürünü olması.
