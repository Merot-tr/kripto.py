import customtkinter as ctk
import base64
import codecs

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class KriptoV22:
    def __init__(self, root):
        self.root = root
        self.root.title("Jek the Rıpır v2.2 - Pro Logic")
        self.root.geometry("500x650")
        
        ctk.CTkLabel(self.root, text="KRİPTO İŞLEM MERKEZİ", font=("Courier New", 22, "bold"), text_color="#17a2b8").pack(pady=20)

        self.giriş_kutusu = ctk.CTkTextbox(self.root, width=400, height=100, border_width=1)
        self.giriş_kutusu.pack(pady=10)

        self.algoritma_secici = ctk.CTkOptionMenu(self.root, 
            values=["Sezar (+3)", "XOR (123)", "Ters Çevir", "Base64", "ROT13", "Atbash", "Hex (Onaltılık)"])
        self.algoritma_secici.pack(pady=10)

        # Çift Buton Yapısı
        btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        btn_frame.pack(pady=15)

        self.btn_sifrele = ctk.CTkButton(btn_frame, text="ŞİFRELE", command=lambda: self.islem_yap("sifrele"), fg_color="#28a745")
        self.btn_sifrele.grid(row=0, column=0, padx=10)

        self.btn_coz = ctk.CTkButton(btn_frame, text="ÇÖZ", command=lambda: self.islem_yap("coz"), fg_color="#dc3545")
        self.btn_coz.grid(row=0, column=1, padx=10)

        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=400, height=120, border_width=1, border_color="#17a2b8")
        self.sonuc_kutusu.pack(pady=10)

    def islem_yap(self, mod):
        ham_metin = self.giriş_kutusu.get("1.0", "end-1c")
        secim = self.algoritma_secici.get()
        sonuc = ""

        match secim:
            case "Sezar (+3)":
                kaydirma = 3 if mod == "sifrele" else -3
                sonuc = "".join(chr(ord(c) + kaydirma) for c in ham_metin)
            case "XOR (123)":
                sonuc = "".join(chr(ord(c) ^ 123) for c in ham_metin) # XOR her iki yönde aynıdır
            case "Ters Çevir":
                sonuc = ham_metin[::-1]
            case "Base64":
                try:
                    if mod == "sifrele":
                        sonuc = base64.b64encode(ham_metin.encode()).decode()
                    else:
                        sonuc = base64.b64decode(ham_metin.encode()).decode()
                except: sonuc = "HATA: Geçersiz Base64 verisi!"
            case "ROT13":
                sonuc = codecs.encode(ham_metin, 'rot_13')
            case "Atbash":
                alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
                ters_alfabe = "zyvüutşsrpoönmlkjiıhğgfedçcbaZYVÜUTŞSRPOÖNMLKJİIĞGFEDÇCBA"
                sonuc = ham_metin.translate(str.maketrans(alfabe, ters_alfabe))
            case "Hex (Onaltılık)":
                try:
                    if mod == "sifrele":
                        sonuc = ham_metin.encode().hex()
                    else:
                        sonuc = bytes.fromhex(ham_metin).decode()
                except: sonuc = "HATA: Geçersiz Hex verisi!"

        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", sonuc)

if __name__ == "__main__":
    app = ctk.CTk()
    KriptoV22(app)
    app.mainloop()

