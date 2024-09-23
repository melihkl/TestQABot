# Test Mühendisliği Chatbot

Bu proje, test mühendisliği ile ilgili sorulara cevap veren bir chatbot sistemidir. Proje, FastAPI ile oluşturulan bir backend ve Vue.js ile geliştirilen bir frontend içerir.

## Proje Yapısı

## Kullanım

### Backend

1. **Backend'i çalıştırmak için:**
   - Gerekli paketleri yükle:
     ```bash
     pip install -r requirements.txt
     ```
   - FastAPI uygulamasını başlat:
     ```bash
     uvicorn main:app --reload
     ```
   - Backend varsayılan olarak `http://localhost:8000` adresinde çalışacaktır.

### Frontend

1. **Frontend'i çalıştırmak için:**
   - Gerekli paketleri yükle:
     ```bash
     npm install
     ```
   - Vue.js uygulamasını başlat:
     ```bash
     npm run serve
     ```
   - Frontend varsayılan olarak `http://localhost:8080` adresinde çalışacaktır.

## API

### Soruları Getir

- **GET /questions**
  
  Tüm soruların listesini döner.

### Soru Sor

- **POST /ask**
  
  Soru sormak için kullanılır. Gövde örneği:
  ```json
  {
    "text": "Test mühendisliği nedir?"
  }
