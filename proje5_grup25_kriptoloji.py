import customtkinter as ctk
from tkinter import filedialog
import base64
import codecs

class KriptoV23:
    def __init__(self, root):
        self.root = root
        self.root.title("Jek the Rıpır v2.3 - File & Crypto")
        self.root.geometry("550x700")
        
        # Başlık ve Dosya Butonu
        ctk.CTkLabel(self.root, text="DOSYA TABANLI KRİPTO", font=("Courier New", 22, "bold"), text_color="#6f42c1").pack(pady=15)
        
        self.btn_dosya = ctk.CTkButton(self.root, text="📁 TXT DOSYASI SEÇ", command=self.dosya_oku, fg_color="#444", hover_color="#555")
        self.btn_dosya.pack(pady=5)

        self.giriş_kutusu = ctk.CTkTextbox(self.root, width=450, height=120)
        self.giriş_kutusu.pack(pady=10)

        self.algoritma_secici = ctk.CTkOptionMenu(self.root, 
            values=["Sezar (+3)", "XOR (123)", "Ters Çevir", "Base64", "ROT13", "Atbash", "Hex (Onaltılık)"],
fg_color="#6f42c1", button_color="#5a32a3")
        self.algoritma_secici.pack(pady=10)

        # İşlem Butonları
        btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="ŞİFRELE", command=lambda: self.islem_yap("sifrele"), fg_color="#28a745").grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="ÇÖZ", command=lambda: self.islem_yap("coz"), fg_color="#dc3545").grid(row=0, column=1, padx=10)

        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=450, height=120, border_color="#6f42c1", border_width=1)
        self.sonuc_kutusu.pack(pady=10)

    def dosya_oku(self):
        yol = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
        if yol:
            with open(yol, "r", encoding="utf-8") as f:
                self.giriş_kutusu.delete("1.0", "end")
                self.giriş_kutusu.insert("1.0", f.read())

    def islem_yap(self, mod):
        # Match-case mantığı v2.2 ile aynı, çözme özellikleri dahil
        ham_metin = self.giriş_kutusu.get("1.0", "end-1c")
        secim = self.algoritma_secici.get()
        sonuc = ""

        match secim:
            case "Sezar (+3)":
                k = 3 if mod == "sifrele" else -3
                sonuc = "".join(chr(ord(c) + k) for c in ham_metin)
            case "XOR (123)":
                sonuc = "".join(chr(ord(c) ^ 123) for c in ham_metin)
            case "Ters Çevir":
                sonuc = ham_metin[::-1]
            case "Base64":
                try:
                    sonuc = base64.b64encode(ham_metin.encode()).decode() if mod == "sifrele" else base64.b64decode(ham_metin.encode()).decode()
                except: sonuc = "HATA!"
            case "ROT13":
                sonuc = codecs.encode(ham_metin, 'rot_13')
            case "Atbash":
                a = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
                t = "zyvüutşsrpoönmlkjiıhğgfedçcbaZYVÜUTŞSRPOÖNMLKJİIĞGFEDÇCBA"
                sonuc = ham_metin.translate(str.maketrans(a, t))
            case "Hex (Onaltılık)":
                try:
                    sonuc = ham_metin.encode().hex() if mod == "sifrele" else bytes.fromhex(ham_metin).decode()
                except: sonuc = "HATA!"

        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", sonuc)

if __name__ == "__main__":
    app = ctk.CTk()
    KriptoV23(app)
    app.mainloop()
