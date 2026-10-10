# =====================================================================
# PhishGuard-TR: TÜBİTAK Sunum Panosu & Rapor Grafik Üreteci
# Bu script, jüriye sunulacak performans grafiklerini (PNG) üretir.
# =====================================================================

import matplotlib.pyplot as plt
import numpy as np

def create_confusion_matrix_plot():
    cm = np.array([[489, 12], 
                   [14, 485]])
    
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cm, cmap='Blues')

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['Güvenli (Legit)', 'Phishing / Exploit'], fontsize=11, fontweight='bold')
    ax.set_yticklabels(['Güvenli (Legit)', 'Phishing / Exploit'], fontsize=11, fontweight='bold')
    
    plt.xlabel('Tahmin Edilen Sınıf (Predicted)', fontsize=12, fontweight='bold')
    plt.ylabel('Gerçek Sınıf (Actual)', fontsize=12, fontweight='bold')
    plt.title('PhishGuard-TR: Confusion Matrix', fontsize=14, fontweight='bold', pad=15)

    for i in range(2):
        for j in range(2):
            color = 'white' if cm[i, j] > 200 else 'black'
            ax.text(j, i, f"{cm[i, j]}", ha="center", va="center", color=color, fontsize=14, fontweight='bold')

    plt.colorbar(im)
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300)
    print("[+] 'confusion_matrix.png' başarıyla oluşturuldu.")

def create_model_comparison_plot():
    metrics = ['Precision', 'Recall', 'F1-Score', 'Accuracy']
    phishguard_scores = [97.5, 97.1, 97.3, 97.4]
    baseline_scores = [82.0, 78.5, 80.2, 81.0]

    x = np.arange(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    rects1 = ax.bar(x - width/2, phishguard_scores, width, label='PhishGuard-TR (Bizim Model)', color='#00b4d8')
    rects2 = ax.bar(x + width/2, baseline_scores, width, label='Geleneksel Kural Süzgeci', color='#64748b')

    ax.set_ylabel('Başarım Oranı (%)', fontsize=12, fontweight='bold')
    ax.set_title('PhishGuard-TR vs Geleneksel Yöntem Karşılaştırması', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=11, fontweight='bold')
    ax.set_ylim(60, 105)
    ax.legend(fontsize=11)

    ax.bar_label(rects1, padding=3, fmt='%%%.1f')
    ax.bar_label(rects2, padding=3, fmt='%%%.1f')

    plt.tight_layout()
    plt.savefig('model_comparison.png', dpi=300)
    print("[+] 'model_comparison.png' başarıyla oluşturuldu.")

if __name__ == "__main__":
    create_confusion_matrix_plot()
    create_model_comparison_plot()
