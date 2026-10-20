# Kişisel Harcama Analiz Sistemi

Python ve MySQL kullanılarak geliştirilen, kişisel harcamaları kaydetmek ve analiz etmek amacıyla oluşturulmuş bir uygulama.

## Özellikler

- Harcama ekleme
- Kayıtlı harcamaları listeleme
- Harcama güncelleme ve silme
- Toplam harcama tutarını hesaplama
- Kategorilere göre harcama analizi yapma
- Tarih doğrulaması ile hatalı tarih girişlerini önleme
- MySQL veritabanı ile veri saklama

## Kullanılan Teknolojiler

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- Git ve GitHub

## Kurulum

1. Projeyi bilgisayarına indir.
2. Gerekli Python kütüphanelerini yükle.
3. MySQL üzerinde `harcama_db` veritabanını oluştur ve `harcamalar` tablosunu hazırla.
4. Proje klasöründe `.env` dosyasını oluştur ve kendi veritabanı bağlantı bilgilerini tanımla.
5. Uygulamayı çalıştır.

Gerekli ortam değişkenleri:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

**Güvenlik notu:** `.env` dosyası veritabanı bilgilerini içerdiğinden GitHub'a yüklenmemelidir.

## Çalıştırma

```bash
python database.py
```

## Amaç

Bu proje; Python ile veritabanı işlemlerini, CRUD operasyonlarını, kullanıcı girdisi doğrulamayı ve temel veri analizini uygulamalı olarak öğrenmek amacıyla geliştirilmiştir.
