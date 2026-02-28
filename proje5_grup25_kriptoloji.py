import customtkinter as ctk

# Temayı "Cyber" havasına sokalım
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AraSurumKripto:
    def __init__(self, root):
        self.root = root
        self.root.title("Jek the Rıpır - Lite Pro")
        self.root.geometry("450x550")
        
        # --- UI KURULUMU ---
        # Başlık
        self.label_baslik = ctk.CTkLabel(self.root, text="MODERN ŞİFRELEME", 
                                        font=("Orbitron", 22, "bold"), 
                                        text_color="#00ffcc")
        self.label_baslik.pack(pady=20)

        # Giriş Alanı
        self.giriş_kutusu = ctk.CTkEntry(self.root, placeholder_text="Metni buraya girin...", 
                                         width=350, height=40)
        self.giriş_kutusu.pack(pady=10)

        # Algoritma Seçici (Combo Box)
        self.algoritma_secici = ctk.CTkOptionMenu(self.root, 
                                                  values=["Sezar (+3)", "Ters Çevir", "Base64", "XOR (123)"],
                                                  button_color="#2b2b2b",
                                                  fg_color="#333333")
        self.algoritma_secici.pack(pady=15)

        # Butonlar İçin Frame
        self.btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.btn_sifrele = ctk.CTkButton(self.btn_frame, text="Şifrele", 
                                         fg_color="#1f538d", hover_color="#14375e",
                                         command=self.islem_sifrele, width=120)
        self.btn_sifrele.grid(row=0, column=0, padx=10)

        self.btn_coz = ctk.CTkButton(self.btn_frame, text="Şifreyi Çöz", 
                                      fg_color="#a83232", hover_color="#7a2424",
                                      command=self.islem_coz, width=120)
        self.btn_coz.grid(row=0, column=1, padx=10)

        # Sonuç Alanı
        self.sonuc_label = ctk.CTkLabel(self.root, text="İŞLEM SONUCU", font=("Arial", 10, "bold"))
        self.sonuc_label.pack(pady=(20, 0))

        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=350, height=120, 
                                           border_color="#00ffcc", border_width=1)
        self.sonuc_kutusu.pack(pady=10)

    # --- MANTIK KISMI ---
    def islem_sifrele(self):
        metin = self.giriş_kutusu.get()
        secim = self.algoritma_secici.get()
        sonuc = ""

        if secim == "Sezar (+3)":
            sonuc = "".join(chr(ord(c) + 3) for c in metin)
        elif secim == "Ters Çevir":
            sonuc = metin[::-1]
        elif secim == "Base64":
            import base64
            sonuc = base64.b64encode(metin.encode()).decode()
        elif secim == "XOR (123)":
            sonuc = "".join(chr(ord(c) ^ 123) for c in metin)

        self.yazdir(sonuc)

    def islem_coz(self):
        metin = self.giriş_kutusu.get()
        secim = self.algoritma_secici.get()
        sonuc = ""

        if secim == "Sezar (+3)":
            sonuc = "".join(chr(ord(c) - 3) for c in metin)
        elif secim == "Ters Çevir":
            sonuc = metin[::-1]
        elif secim == "Base64":
            import base64
            try:
                sonuc = base64.b64decode(metin.encode()).decode()
            except:
                sonuc = "HATA: Geçersiz Base64 formatı!"
        elif secim == "XOR (123)":
            sonuc = "".join(chr(ord(c) ^ 123) for c in metin)

        self.yazdir(sonuc)

    def yazdir(self, metin):
        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", metin)

if __name__ == "__main__":
    app = ctk.CTk()
    AraSurumKripto(app)
    app.mainloop()
