import customtkinter as ctk
from tkinter import filedialog
import base64

# Temayı Kali Linux havasına sokalım
ctk.set_appearance_mode("dark")  # Koyu mod
ctk.set_default_color_theme("blue") # Standart mavi ama biz butonlarda özelleştireceğiz

class KriptoUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kali Kripto v2.1 - Cyber Edition")
        self.root.geometry("600x600")
        self.root.configure(fg_color="#0f0f0f") # Arka planı iyice koyulaştır (Kali terminali gibi)

        self.setup_ui()

    def setup_ui(self):
        # Başlık - Turkuaz Kali rengi
        ctk.CTkLabel(self.root, text="Kripto İşlem Merkezi", 
                     font=("Courier New", 26, "bold"), 
                     text_color="#17a2b8").pack(pady=20)

        # Metin Giriş Alanı
        self.metin_kutusu = ctk.CTkTextbox(self.root, width=500, height=100, 
                                           fg_color="#1a1a1a", border_color="#17a2b8", border_width=1)
        self.metin_kutusu.pack(pady=10)

        # Dosya İşlemleri Butonu
        self.btn_dosya = ctk.CTkButton(self.root, text="TXT Dosyası Seç ve Oku", 
                                       fg_color="#2b2b2b", hover_color="#444444",
                                       command=self.dosya_oku)
        self.btn_dosya.pack(pady=5)

        # Algoritma Seçimi - Listeye yeni algoritmalar eklendi
        self.algoritma_secici = ctk.CTkOptionMenu(self.root, 
                                                 fg_color="#17a2b8", 
                                                 button_color="#138496",
                                                 button_hover_color="#117a8b",
                                                 values=["Sezar (+3)", "XOR (123)", "Ters Çevir", 
                                                         "Base64", "ROT13", "Atbash", "Hex (Onaltılık)"])
        self.algoritma_secici.pack(pady=15)

        # İşlem Butonları
        btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Şifrele / İşle", command=self.islem_yap, 
                      fg_color="#28a745", hover_color="#218838").pack(side="left", padx=10)
        
        ctk.CTkButton(btn_frame, text="Kaydet (.txt)", command=self.dosya_kaydet, 
                      fg_color="#6f42c1", hover_color="#5a32a3").pack(side="left", padx=10)

        # Sonuç Alanı
        ctk.CTkLabel(self.root, text="İşlem Sonucu:", font=("Arial", 12)).pack(pady=(10,0))
        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=500, height=100, 
                                           fg_color="#1a1a1a", border_color="#6f42c1", border_width=1)
        self.sonuc_kutusu.pack(pady=10)

    # --- DOSYA FONKSİYONLARI ---
    def dosya_oku(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
        if dosya_yolu:
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                self.metin_kutusu.delete("1.0", "end")
                self.metin_kutusu.insert("1.0", dosya.read())

    def dosya_kaydet(self):
        icerik = self.sonuc_kutusu.get("1.0", "end-1c")
        if icerik.strip():
            dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt")])
            if dosya_yolu:
                with open(dosya_yolu, "w", encoding="utf-8") as dosya:
                    dosya.write(icerik)

    # --- KRİPTO MANTIK ---
    def islem_yap(self):
        ham_metin = self.metin_kutusu.get("1.0", "end-1c")
        secim = self.algoritma_secici.get()
        sonuc = ""

        match secim:
            case "Sezar (+3)":
                sonuc = "".join(chr(ord(c) + 3) for c in ham_metin)
            case "XOR (123)":
                sonuc = "".join(chr(ord(c) ^ 123) for c in ham_metin)
            case "Ters Çevir":
                sonuc = ham_metin[::-1]
            case "Base64":
                sonuc = base64.b64encode(ham_metin.encode()).decode()
            case "ROT13":
                # Alfabedeki harfleri 13 kaydırır (CyberChef'te çok kullanılır)
                import codecs
                sonuc = codecs.encode(ham_metin, 'rot_13')
            case "Atbash":
                # Alfabeyi tersine çevirir (A->Z, B->Y)
                alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
                ters_alfabe = "zyvüutşsrpoönmlkjiıhğgfedçcbaZYVÜUTŞSRPOÖNMLKJİIĞGFEDÇCBA"
                tablo = str.maketrans(alfabe, ters_alfabe)
                sonuc = ham_metin.translate(tablo)
            case "Hex (Onaltılık)":
                # Metni hex koduna çevirir
                sonuc = ham_metin.encode().hex()

        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", sonuc)

if __name__ == "__main__":
    app = ctk.CTk()
    KriptoUygulamasi(app)
    app.mainloop()