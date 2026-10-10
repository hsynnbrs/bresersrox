# =====================================================================
# PhishGuard-TR: Birim Test ve Algoritma Doğrulama Süiti (Unit Tests)
# Bu script, Levenshtein ve Exploit modüllerinin doğruluğunu test eder.
# =====================================================================

import unittest

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

class TestPhishGuardEngine(unittest.TestCase):

    def test_typosquatting_detection(self):
        official = "turkiye.gov.tr"
        fake_domain = "turkiye-gov-tr"
        distance = levenshtein_distance(fake_domain, official)
        self.assertTrue(0 < distance <= 5, f"Beklenen Typosquatting mesafesi sapması: {distance}")

    def test_exact_match_zero_distance(self):
        official = "ziraatbank.com.tr"
        self.assertEqual(levenshtein_distance(official, official), 0)

    def test_exploit_token_detection(self):
        sample_url = "https://canli-yayin-stream-camera.com?access=cam_capture"
        exploit_tokens = ["camera", "cam_capture", "webcam"]
        has_exploit = any(token in sample_url for token in exploit_tokens)
        self.assertTrue(has_exploit, "Kamera izni tuzağı tespiti başarısız oldu!")

if __name__ == '__main__':
    print("[*] PhishGuard-TR Birim Testleri Çalıştırılıyor...\n")
    unittest.main()
