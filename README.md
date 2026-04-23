# CI/CD Pipeline with GitHub Actions

A production-ready CI/CD pipeline that automatically runs tests on every push using GitHub Actions and pytest.

## What it does
Every time code is pushed to the main branch, GitHub automatically spins up a clean Ubuntu machine, installs dependencies, and runs all tests. If tests pass, the code is safe. If they fail, you get notified immediately.

## Tech Stack
- **FastAPI** — High-performance Python web framework
- **HuggingFace Transformers** — DistilBERT sentiment analysis model
- **pytest** — Python testing framework
- **GitHub Actions** — Automated CI/CD pipeline
- **httpx** — HTTP client for testing API endpoints

## Project Structure

```
02-ci-cd-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions workflow
├── app/
│   ├── __init__.py
│   └── main.py           # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_main.py      # Automated tests
├── requirements.txt
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run Tests Locally

```bash
pytest tests/ -v
```

## CI/CD Pipeline

The pipeline runs automatically on every push to main branch:

1. GitHub spins up a clean Ubuntu machine
2. Python 3.11 is installed
3. Dependencies are installed
4. All tests are executed
5. Result is shown as green tick or red cross

## Tests

| Test | Description | Expected Result |
|------|-------------|-----------------|
| test_health_check | Checks if API is running | Status 200, {"status": "ok"} |
| test_predict_positive | Sends positive text | Returns POSITIVE label |
| test_predict_negative | Sends negative text | Returns NEGATIVE label |

## Results

- 3/3 tests passing
- Pipeline execution time: ~1m 28s
- Zero manual intervention required after push

---

## Türkçe Açıklama

GitHub Actions ve pytest kullanilarak her push'ta otomatik test calistiran, production'a hazir bir CI/CD pipeline.

## Ne Yapar?
Main branch'e her kod push edildiginde, GitHub otomatik olarak temiz bir Ubuntu makinesi baslatir, bagimliliklar yukler ve tüm testleri calistirir. Testler gecerse kod güvenlidir. Gecemezse aninda bildirim alirsiniz.

## Teknoloji Yigini
- **FastAPI** — Yüksek performansli Python web framework'ü
- **HuggingFace Transformers** — DistilBERT duygu analizi modeli
- **pytest** — Python test framework'ü
- **GitHub Actions** — Otomatik CI/CD pipeline
- **httpx** — API endpoint'lerini test etmek icin HTTP istemcisi

## Yerel Kurulum

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Testleri Yerel Calistirma

```bash
pytest tests/ -v
```

## CI/CD Pipeline Akisi

Pipeline, main branch'e her push'ta otomatik calisir:

1. GitHub temiz bir Ubuntu makinesi acar
2. Python 3.11 kurulur
3. Bagimliliklar yuklenir
4. Tüm testler calistirilir
5. Sonuc yesil tik veya kirmizi carpi olarak gösterilir

## Testler

| Test | Aciklama | Beklenen Sonuc |
|------|----------|----------------|
| test_health_check | API'nin calisip calismadigini kontrol eder | Durum 200, {"status": "ok"} |
| test_predict_positive | Pozitif metin gönderir | POSITIVE etiketini döndürür |
| test_predict_negative | Negatif metin gönderir | NEGATIVE etiketini döndürür |

## Sonuclar

- 3/3 test gecti
- Pipeline çalisma süresi: ~1dk 28sn
- Push sonrasi sifir manuel müdahale gerekir