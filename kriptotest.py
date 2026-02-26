import customtkinter as ctk
from tkinter import filedialog
import base64
import codecs

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class KriptoUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kali Kripto v2.2 - Encrypt & Decrypt")
        self.root.geometry("600x680")
        self.root.configure(fg_color="#0f0f0f")

        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self.root, text="Kripto İşlem Merkezi", 
                     font=("Courier New", 26, "bold"), 
                     text_color="#17a2b8").pack(pady=20)

        # Metin Giriş Alanı
        self.metin_kutusu = ctk.CTkTextbox(self.root, width=500, height=100, 
                                           fg_color="#1a1a1a", border_color="#17a2b8", border_width=1)
        self.metin_kutusu.pack(pady=10)

        # Algoritma Seçimi
        self.algoritma_secici = ctk.CTkOptionMenu(self.root, fg_color="#17a2b8", 
                                                 values=["Sezar (+3)", "XOR (123)", "Ters Çevir", 
                                                         "Base64", "ROT13", "Atbash", "Hex (Onaltılık)"])
        self.algoritma_secici.pack(pady=10)

        # İŞLEM TİPİ SEÇİMİ (Şifrele mi, Çöz mü?)
        self.islem_tipi = ctk.CTkSegmentedButton(self.root, values=["Şifrele", "Çöz"],
                                                selected_color="#17a2b8", unselected_color="#2b2b2b")
        self.islem_tipi.set("Şifrele") # Varsayılan olarak Şifrele seçili
        self.islem_tipi.pack(pady=10)

        # Butonlar
        btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="ÇALIŞTIR", command=self.islem_yap, 
                      fg_color="#28a745", hover_color="#218838", width=200).pack(side="left", padx=10)

        # Sonuç Alanı
        ctk.CTkLabel(self.root, text="İşlem Sonucu:", font=("Arial", 12)).pack(pady=(15,0))
        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=500, height=100, 
                                           fg_color="#1a1a1a", border_color="#6f42c1", border_width=1)
        self.sonuc_kutusu.pack(pady=10)

    def islem_yap(self):
        ham_metin = self.metin_kutusu.get("1.0", "end-1c")
        secim = self.algoritma_secici.get()
        tip = self.islem_tipi.get()
        sonuc = ""

        try:
            if tip == "Şifrele":
                match secim:
                    case "Sezar (+3)": sonuc = "".join(chr(ord(c) + 3) for c in ham_metin)
                    case "XOR (123)": sonuc = "".join(chr(ord(c) ^ 123) for c in ham_metin)
                    case "Ters Çevir": sonuc = ham_metin[::-1]
                    case "Base64": sonuc = base64.b64encode(ham_metin.encode()).decode()
                    case "ROT13": sonuc = codecs.encode(ham_metin, 'rot_13')
                    case "Atbash": 
                        alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
                        ters = "zyvüutşsrpoönmlkjiıhğgfedçcbaZYVÜUTŞSRPOÖNMLKJİIĞGFEDÇCBA"
                        sonuc = ham_metin.translate(str.maketrans(alfabe, ters))
                    case "Hex (Onaltılık)": sonuc = ham_metin.encode().hex()
            else: # ÇÖZME İŞLEMİ
                match secim:
                    case "Sezar (+3)": sonuc = "".join(chr(ord(c) - 3) for c in ham_metin)
                    case "XOR (123)": sonuc = "".join(chr(ord(c) ^ 123) for c in ham_metin)
                    case "Ters Çevir": sonuc = ham_metin[::-1]
                    case "Base64": sonuc = base64.b64decode(ham_metin.encode()).decode()
                    case "ROT13": sonuc = codecs.decode(ham_metin, 'rot_13')
                    case "Atbash":
                        alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
                        ters = "zyvüutşsrpoönmlkjiıhğgfedçcbaZYVÜUTŞSRPOÖNMLKJİIĞGFEDÇCBA"
                        sonuc = ham_metin.translate(str.maketrans(ters, alfabe))
                    case "Hex (Onaltılık)": sonuc = bytes.fromhex(ham_metin).decode('utf-8')

        except Exception as e:
            sonuc = f"HATA: Geçersiz format! ({str(e)})"

        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", sonuc)

if __name__ == "__main__":
    app = ctk.CTk()
    KriptoUygulamasi(app)
    app.mainloop()