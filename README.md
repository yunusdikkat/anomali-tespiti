
# 🧠 Ağ Trafiği Anomali Tespiti Projesi

Bu proje, **CICIDS2017** veri seti kullanılarak geliştirilmiş bir **makine öğrenmesi tabanlı ağ trafiği anomali tespit sistemidir**.  
Amaç; normal (BENIGN) ve anormal (BruteForce, DDoS, PortScan gibi) ağ trafiği örneklerini sınıflandırmak ve kullanıcıya sade bir web arayüzü ile sonuç sunmaktır.

---

## 📂 Proje Yapısı

```
anomali-tespiti/
├── data/                    # Örnek CSV veri dosyaları
├── models/                 # Eğitilmiş model dosyası (.pkl)
├── notebooks/              # Veri analizi ve model eğitim adımları
│   ├── 01_Veriyi_İncele.ipynb
│   ├── 02_Model_Eğitimi.ipynb
│   ├── 03_Modeli_Kaydet.ipynb
├── 04_Web_Arayuz/
│   ├── app.py              # Flask uygulaması
│   ├── templates/
│   │   └── index.html      # Web arayüzü
│   └── static/
│       └── style.css       # Stil dosyası
├── README.md               # Proje dökümantasyonu
├── requirements.txt        # Gerekli Python kütüphaneleri
└── .gitignore              # Gereksiz dosyalar
```

---

## 🛠 Kullanılan Teknolojiler

- Python 3
- pandas, scikit-learn, imblearn
- Flask (web uygulaması)
- CICIDS2017 veri seti
- SMOTE (sınıf dengesizliği çözümü)
- Random Forest algoritması

---

## 📈 Model Eğitimi

1. CICIDS2017 verisinden örnek veri alınarak ön işleme yapıldı.
2. `Label` sınıfı `LabelEncoder` ile sayısallaştırıldı.
3. `SMOTE` uygulanarak veriler dengelendi.
4. `RandomForestClassifier` modeli ile eğitim gerçekleştirildi.
5. Model `.pkl` dosyasına kaydedildi.

---

## 🚀 Web Arayüzü Kullanımı

### 🔧 1. Gereksinimleri yükle

```bash
pip install -r requirements.txt
```

### ▶ 2. Flask uygulamasını çalıştır

```bash
cd 04_Web_Arayuz
python app.py
```

Tarayıcıda şu adresi aç:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🧪 3. Web arayüzünden test yap

Formu doldurarak tahmin yapabilir veya “🔁 Örnek Verileri Doldur” butonuna tıklayarak hızlı test gerçekleştirebilirsiniz.

> Tahmin sonucu "BENIGN" (temiz trafik) veya "BruteForce", "DDoS", "PortScan" (anormal trafik) olarak gelir.

---

## 🖼 Arayüz Ekran Görüntüsü

> ![arayüz](docs/preview.png) *(isteğe bağlı ekran görüntüsü eklenecekse bu dosyayı `docs/` altına koy)*

---

## 🧪 Test Sonuçları

| Sınıf        | Precision | Recall | F1 Score |
|--------------|-----------|--------|----------|
| BENIGN       | 0.76      | 0.61   | 0.68     |
| BruteForce   | 0.86      | 0.96   | 0.91     |
| DDoS         | 0.80      | 0.81   | 0.81     |
| PortScan     | 0.81      | 0.87   | 0.84     |
| **Genel**    | **0.81**  | **0.81**| **0.81** |

> SMOTE sonrası başarı oranı dengeli ve güçlüdür.

---

## 📌 Geliştirme Fikirleri

- [ ] CSV dosyası yükleyerek toplu tahmin
- [ ] Flask API (REST endpoint) desteği
- [ ] Kullanıcı paneli/loglama
- [ ] Docker ile konteynerleştirme
- [ ] Canlı ağ verisi ile test ortamı (GNS3 entegrasyonu)

---

