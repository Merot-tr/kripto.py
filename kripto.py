import customtkinter as ctk

def sifrele():
    metin = giriş_kutusu.get()
    # Çok basit bir şifreleme mantığı: Her karakterin kodunu 3 artır
    sifreli = "".join(chr(ord(c) + 3) for c in metin)
    sonuc_etiketi.configure(text=f"Sonuç: {sifreli}")

def coz():
    metin = giriş_kutusu.get()
    # Şifreyi çözmek için 3 geri git
    orijinal = "".join(chr(ord(c) - 3) for c in metin)
    sonuc_etiketi.configure(text=f"Sonuç: {orijinal}")

# Arayüz Ayarları
app = ctk.CTk()
app.geometry("400x300")
app.title("Jek the rıpır")

giriş_kutusu = ctk.CTkEntry(app, placeholder_text="Metni buraya yazın...", width=300)
giriş_kutusu.pack(pady=20)

btn_sifrele = ctk.CTkButton(app, text="Şifrele", command=sifrele)
btn_sifrele.pack(pady=10)

btn_coz = ctk.CTkButton(app, text="Şifreyi Çöz", command=coz)
btn_coz.pack(pady=10)

sonuc_etiketi = ctk.CTkLabel(app, text="Sonuç burada görünecek")
sonuc_etiketi.pack(pady=20)

app.mainloop()