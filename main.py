import tkinter as tk
from tkinter import messagebox # Uyarı pencereleri için (Hata/Başarı mesajı)
import sqlite3

# --- VERİTABANI FONKSİYONU ---
def veritabanina_ekle(baslik, yazar, durum):
    # 1. Veritabanına bağlan
    baglanti = sqlite3.connect("ajanda.db")
    imlec = baglanti.cursor()
    
    # 2. SQL Komutu ile veriyi ekle
    # (Parantez içindeki soru işaretleri güvenlik içindir)
    imlec.execute("INSERT INTO kitaplar (baslik, yazar, durum) VALUES (?, ?, ?)", (baslik, yazar, durum))
    
    # 3. Kaydet ve Kapat
    baglanti.commit()
    baglanti.close()

# --- PENCERE FONKSİYONLARI ---
def kitap_ekle_penceresi():
    # Yeni bir 'yavru' pencere aç (Toplevel)
    yeni_pencere = tk.Toplevel(pencere)
    yeni_pencere.title("Kitap Ekle")
    yeni_pencere.geometry("400x400")

    # -- Kitap Adı --
    tk.Label(yeni_pencere, text="Kitap Adı:").pack(pady=5)
    giris_baslik = tk.Entry(yeni_pencere) # Yazı yazma kutusu
    giris_baslik.pack(pady=5)

    # -- Yazar --
    tk.Label(yeni_pencere, text="Yazar:").pack(pady=5)
    giris_yazar = tk.Entry(yeni_pencere)
    giris_yazar.pack(pady=5)

    # -- Durum (Okudum/Okuyorum) --
    tk.Label(yeni_pencere, text="Durum (Okudum/Okuyorum):").pack(pady=5)
    giris_durum = tk.Entry(yeni_pencere)
    giris_durum.pack(pady=5)

    # -- KAYDET BUTONU --
    # Bu butona basınca ne olacağını içerdeki 'kaydet' fonksiyonuyla belirliyoruz
    def kaydet():
        # Kutulardaki yazıları al (.get() komutu ile)
        ad = giris_baslik.get()
        yazari = giris_yazar.get()
        durumu = giris_durum.get()

        if ad and yazari: # Eğer kutular boş değilse
            veritabanina_ekle(ad, yazari, durumu) # Veritabanı fonksiyonunu çağır
            messagebox.showinfo("Başarılı", "Kitap başarıyla kaydedildi!") # Ekrana mesaj ver
            yeni_pencere.destroy() # Küçük pencereyi kapat
        else:
            messagebox.showwarning("Hata", "Lütfen kitap adı ve yazarı girin.")

    tk.Button(yeni_pencere, text="KAYDET", command=kaydet, bg="green", fg="white").pack(pady=20)


def film_ekle_tikla():
    # Şimdilik burası boş kalsın
    messagebox.showinfo("Bilgi", "Film modülü bir sonraki adımda yapılacak!")

# --- ANA ARAYÜZ ---
pencere = tk.Tk()
pencere.title("Kültür Ajandası")
pencere.geometry("500x400")

baslik = tk.Label(pencere, text="Kültür & Sanat Ajandam", font=("Arial", 20, "bold"))
baslik.pack(pady=20)

# Butonlar
btn_kitap = tk.Button(pencere, text="📚 Yeni Kitap Ekle", font=("Arial", 12), command=kitap_ekle_penceresi)
btn_kitap.pack(pady=10)

btn_film = tk.Button(pencere, text="🎬 Yeni Film Ekle", font=("Arial", 12), command=film_ekle_tikla)
btn_film.pack(pady=10)

# Programı çalıştır
pencere.mainloop()