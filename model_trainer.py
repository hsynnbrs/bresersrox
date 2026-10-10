# =====================================================================
# PhishGuard-TR: Makine Öğrenmesi Model Eğitimi ve Metrik Çıkarım Kodu
# Metodoloji: TF-IDF Metin Vektörleştirme ve Random Forest Sınıflandırıcı
# =====================================================================

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

dataset = {
    'text': [
        "e-devlet kapisi aidat iadeniz onaylanmistir tikla alin",
        "Sayin musterimiz hesabiniz gecici olarak durduruldu sitemizden guncelleyin",
        "Kargonuz adres yetersizliginden teslim edilemedi hemen adres yazin",
        "e-Devlet Kapısı üzerinden randevu talebiniz başarıyla oluşturulmuştur",
        "Sayın abonemiz fatura ödemeniz başarıyla gerçekleşmiştir detaylar için girin",
        "Tebrikler 10000 TL hediye çarkını çevirmek ve kazanmak için tıkla",
        "Hesabınıza yetkisiz erişim tespit edildi şifrenizi hemen sıfırlayın",
        "Ziraat Bankası internet bankacılığı şifre yenileme talebiniz alınmıştır",
        "Ceza dosyanız icra takibine alınmıştır hemen ödeme yapmak için tıklayın",
        "GİB vergi borcu ödeme işleminiz başarıyla tamamlanmıştır"
    ],
    'label': [1, 1, 1, 0, 0, 1, 1, 0, 1, 0]  # 1: Phishing, 0: Legitimate
}

df = pd.DataFrame(dataset)

vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=2500, lowercase=True)
X = vectorizer.fit_transform(df['text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("--- MODEL EVALUATION REPORT ---")
print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing']))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
