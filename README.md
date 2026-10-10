# 🛡️ PhishGuard-TR: Akıllı Türkçe Oltalama & Donanım Tuzağı Tespit Platformu

[![TÜBİTAK 2026](https://img.shields.io/badge/T%C3%9CB%C4%B0TAK-2026%20Projesi-00b4d8.svg)](https://hsynnbrs.github.io/PhishGuard-TR/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

**PhishGuard-TR**, Türkçe sosyal mühendislik tuzaklarını, harf oyunlarıyla yapılan sahte alan adı taklitlerini (Typosquatting) ve tarayıcı tabanlı donanım/kamera izni tuzaklarını (Exploit/Permission Phishing) tespit etmek amacıyla geliştirilmiş hibrit bir siber güvenlik platformudur.

---

## 🚀 Öne Çıkan Özellikler

- **🔤 Levenshtein Harf Mesafesi Matrisi ($D(s_1, s_2)$):** Orijinal devlet ve banka domainleri ile şüpheli domainler arasındaki matematiksel düzenleme mesafesini hesaplar.
- **🧠 Türkçe NLP & Sosyal Mühendislik Analizi:** Panik, aciliyet ve ödül algısı oluşturan Türkçe kelime kalıplarını vektörel olarak süzgeçten geçirir.
- **📷 Donanım & Kamera Exploit Taraması:** İzinsiz kamera/mikrofon erişimi veya medya yakalama kurgulayan şüpheli bağlantıları tespit eder.
- **📊 Model Metrikleri & Confusion Matrix:** %97.3 F1-Score başarısına sahip yapay zeka model analizi.

---

## 📈 Model Başarım Metrikleri

| Metrik | Değer |
| :--- | :--- |
| **Precision (Hassasiyet)** | %97.5 |
| **Recall (Duyarlılık)** | %97.1 |
| **F1-Score** | **%97.3** |
| **Çıkarım Süresi (Inference)** | ~0.024s |
