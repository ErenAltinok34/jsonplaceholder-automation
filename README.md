# JSONPlaceholder API Tests

Bu proje, [JSONPlaceholder](https://jsonplaceholder.typicode.com/) sahte API'si üzerinde Python `pytest` ve `requests` kütüphaneleri kullanılarak yazılmış temel API testlerini içerir.

## İçindekiler

- Kullanıcı (`users`) endpoint testleri
- Gönderi (`posts`) endpoint testleri
- `pytest-html` ile HTML test raporu oluşturma
- Basit API otomasyon testi örneği

## Kurulum

1. Python 3.7+ yüklü olmalı.

2. Sanal ortam oluştur ve aktif et:

```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/Mac için:
source venv/bin/activate
