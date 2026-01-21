import sqlite3

# Veritabanı dosyasına bağlan (yoksa otomatik oluşturur)
baglanti = sqlite3.connect("ajanda.db")
imlec = baglanti.cursor()

# 1. Kitaplar tablosunu oluştur
imlec.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    baslik TEXT,
    yazar TEXT,
    durum TEXT,
    puan INTEGER,
    notlar TEXT
)
""")

# 2. Filmler tablosunu oluştur
imlec.execute("""
CREATE TABLE IF NOT EXISTS filmler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adi TEXT,
    yonetmen TEXT,
    tarih TEXT,
    puan INTEGER,
    yorumlar TEXT
)
""")

# 3. Ajanda tablosunu oluştur
imlec.execute("""
CREATE TABLE IF NOT EXISTS ajanda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarih TEXT,
    baslik TEXT,
    icerik TEXT
)
""")

# İşlemleri kaydet ve kapat
baglanti.commit()
baglanti.close()

print("Tebrikler! ajanda.db dosyası başarıyla oluşturuldu.")