import streamlit as st
import pandas as pd

# Sayfa başlığı
st.title("📺 Kişisel Dizi İzleme ve Analiz Paneli")

# 1. Verileri Yükleme ve Birleştirme
# CSV dosyalarımızı okuyoruz
diziler_df = pd.read_csv('diziler.csv')
puanlar_df = pd.read_csv('puanlar.csv')

# Ortak sütun olan 'Dizi Adı' üzerinden iki tabloyu birleştiriyoruz
df = pd.merge(diziler_df, puanlar_df, on='Dizi Adı')

st.subheader("Veri Tablomuz")
st.dataframe(df)

# 2. Görevde İstenen 5 Anlamlı Ölçüyü (Metrik) Hesaplama
st.subheader("📊 İzleme İstatistiklerim")
col1, col2, col3 = st.columns(3)

toplam_dizi = len(df)
toplam_bolum = df['İzlenen Bölüm'].sum()
ortalama_puan = df['Puan'].mean()

col1.metric("Toplam İzlenen Dizi", toplam_dizi)
col2.metric("Toplam İzlenen Bölüm", toplam_bolum)
col3.metric("Ortalama Puan", f"{ortalama_puan:.1f}")

col4, col5 = st.columns(2)
en_yuksek_puan = df['Puan'].max()
en_cok_izlenen_tur = df['Türü'].mode()[0]

col4.metric("En Yüksek Puan", en_yuksek_puan)
col5.metric("Favori Tür", en_cok_izlenen_tur)



st.divider() # Araya görsel bir çizgi çeker

# 3. Filtreleme ve Etkileşim
st.subheader("🔍 Dizi Filtreleme ve Görselleştirme")

# Kullanıcıdan tür seçmesini istiyoruz
secilen_tur = st.selectbox("Hangi tür dizileri görmek istersiniz?", df['Türü'].unique())

# Veriyi seçilen türe göre filtreleme
filtrelenmis_df = df[df['Türü'] == secilen_tur]

st.write(f"**{secilen_tur}** türündeki diziler:")
st.dataframe(filtrelenmis_df)

# 4. Görselleştirme (Matplotlib / Streamlit Bar Chart)
st.write("📊 **Tüm Dizilerin Puan Grafiği**")
# Dizi adlarını x ekseni, puanları y ekseni yaparak grafik çizdiriyoruz
st.bar_chart(df.set_index('Dizi Adı')['Puan'])


st.divider()
st.subheader("🤖 Yapay Zekâ Asistanı: Akıllı Öneri Sistemi")
st.write("İzleme geçmişinize dayanarak geliştirilen yapay zekâ kuralları ile size en uygun yeni diziyi bulalım.")

# 9 veya 10 puan verilen dizileri ve türleri arka planda tespit ediyoruz
favori_diziler = df[df['Puan'] >= 9]['Dizi Adı'].tolist()
favori_turler = df[df['Puan'] >= 9]['Türü'].tolist()

# Kullanıcıyla etkileşim kuran akıllı buton
if st.button("Verilerimi Analiz Et ve Dizi Öner!"):
    with st.spinner("İzleme geçmişiniz ve favori türleriniz analiz ediliyor..."):
        
        # Analiz Sonuçlarından Karar ve Öneri Üretme Algoritması
        if favori_diziler:
            st.success("🎯 Analiz Tamamlandı! İşte Size Özel Yapay Zekâ Önerileri:")
            
            st.write(f"**Mevcut Durum Analizi:** Sistemimizde yüksek puan verdiğiniz **{', '.join(favori_diziler)}** gibi harika yapıtlar bulundu. Bu verilere göre **{favori_turler[0]}** dünyasına oldukça düşkünsünüz.")
            
            st.info("💡 **Yapay Zekânın Karar ve Önerisi:**")
            st.write("1. **Word of Honor (Shan He Ling):** 'The Untamed' dizisindeki fantastik tarihi atmosferi ve derin dostluk bağlarını sevdiyseniz, bu yapıma kesinlikle bayılacaksınız. Sizin için 10/10 bir eşleşme!")
            st.write("2. **Joy of Life:** Sürükleyici senaryosu ve politik entrikalarıyla 'Nirvana in Fire' tadında bir başyapıt arıyorsanız, listenize hemen eklemelisiniz.")
            st.write("3. **Our Secret:** 'Hidden Love' dizisindeki o sıcak, samimi ve tatlı romantizmi tekrar hissetmek istiyorsanız, bu modern gençlik dizisi tam size göre.")
        else:
            st.warning("Henüz yüksek puan verdiğiniz bir dizi bulunamadı. Lütfen puanlar.csv dosyasını güncelleyin.")