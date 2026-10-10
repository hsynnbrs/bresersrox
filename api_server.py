# =====================================================================
# PhishGuard-TR: Enterprise REST API Service
# TÜBİTAK Projesi - Arka Plan API Sunucu Altyapısı
# =====================================================================

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="PhishGuard-TR API",
    description="Türkçe Phishing & Exploit Analiz Servisi",
    version="1.0.0"
)

class ThreatCheckRequest(BaseModel):
    url: str = None
    text: str = None

def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

LEGIT_DOMAINS = ["turkiye.gov.tr", "egm.gov.tr", "gib.gov.tr", "ziraatbank.com.tr"]
EXPLOIT_TOKENS = ["camera", "kamera", "webcam", "mic-access", "cam_capture", "canli-yayin"]

@app.post("/api/v1/scan")
def scan_threat(payload: ThreatCheckRequest):
    risk_score = 0
    reasons = []
    
    combined = f"{payload.url or ''} {payload.text or ''}".lower()
    
    matched_exploits = [token for token in EXPLOIT_TOKENS if token in combined]
    if matched_exploits:
        risk_score += 85
        reasons.append(f"Kamera/Donanım tuzağı parametreleri tespit edildi: {matched_exploits}")

    if payload.url:
        clean_url = payload.url.replace("https://", "").replace("http://", "").split("/")[0]
        for legit in LEGIT_DOMAINS:
            dist = levenshtein_distance(clean_url, legit)
            if 0 < dist <= 5:
                risk_score += 75
                reasons.append(f"Typosquatting Taklidi ({legit} ile Levenshtein Mesafesi: {dist})")

    risk_score = min(risk_score, 99)
    status = "TEHDİT" if risk_score >= 50 else "GÜVENLİ"

    return {
        "status": status,
        "risk_score": risk_score,
        "details": reasons,
        "model_version": "PhishGuard-TR-v1.0"
    }
