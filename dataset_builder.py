# =====================================================================
# PhishGuard-TR: Veri Seti Oluşturucu ve Ön İşleme (Preprocessing)
# Ham Türkçe oltalama verilerini NLP modeline uygun CSV formatına getirir.
# =====================================================================

import pandas as pd
import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '[LINK]', text)
    text = re.sub(r'[^a-zıaşğöçü0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

raw_data = [
    {"content": "Tebrikler! Kart aidat iadenizi hemen almak için [LINK] adresine tıklayın.", "label": 1},
    {"content": "e-Devlet Kapısı kapalı randevu talebiniz başarıyla güncellenmiştir.", "label": 0},
    {"content": "Hesabınız geçici olarak kısıtlandı. Şifrenizi yenilemek için tıklayınız.", "label": 1},
    {"content": "Sayın abonemiz, bu ayki faturanız 145 TL olarak gerçekleşmiştir.", "label": 0},
    {"content": "Ceza dosyanız icra takibine düşmüştür, ödemek için hemen giriş yapın.", "label": 1},
    {"content": "Görüntülü görüşmeyi başlatmak için kamera iznini onaylayın [LINK].", "label": 1}
]

print("[*] Ham metinler temizleniyor ve vektörleştirmeye hazırlanıyor...")
df = pd.DataFrame(raw_data)
df['cleaned_content'] = df['content'].apply(clean_text)

df.to_csv('processed_dataset.csv', index=False, encoding='utf-8')
print("[+] 'processed_dataset.csv' başarıyla oluşturuldu!")
print(df[['cleaned_content', 'label']].head())
