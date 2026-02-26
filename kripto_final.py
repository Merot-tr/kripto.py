import customtkinter as ctk
from tkinter import filedialog # Dosya seçme penceresi için

class KriptoUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kripto v2.0 - Dosya ve Çoklu Algoritma")
        self.root.geometry("600x550")

        # UI Kurulumu
        self.setup_ui()

    def setup_ui(self):
        # Başlık
        ctk.CTkLabel(self.root, text="Kripto İşlem Merkezi", font=("Arial", 22, "bold")).pack(pady=20)

        # Metin Giriş Alanı
        self.metin_kutusu = ctk.CTkTextbox(self.root, width=500, height=100)
        self.metin_kutusu.pack(pady=10)

        # Dosya İşlemleri Butonu
        self.btn_dosya = ctk.CTkButton(self.root, text="TXT Dosyası Seç ve Oku", fg_color="#1f538d",
                                       command=self.dosya_oku)
        self.btn_dosya.pack(pady=5)

        # Algoritma Seçimi
        self.algoritma_secici = ctk.CTkOptionMenu(self.root, 
                                                 values=["Sezar (+3)", "XOR (123)", "Ters Çevir", "Base64 (Kodlama)"])
        self.algoritma_secici.pack(pady=10)

        # İşlem Butonları
        btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Şifrele / İşle", command=self.islem_yap, fg_color="green").pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Kaydet (.txt)", command=self.dosya_kaydet, fg_color="orange").pack(side="left", padx=10)

        # Sonuç Alanı
        self.sonuc_kutusu = ctk.CTkTextbox(self.root, width=500, height=100)
        self.sonuc_kutusu.pack(pady=20)

    # --- DOSYA FONKSİYONLARI ---
    def dosya_oku(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
        if dosya_yolu:
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                icerik = dosya.read()
                self.metin_kutusu.delete("1.0", "end")
                self.metin_kutusu.insert("1.0", icerik)

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
            case "Base64 (Kodlama)":
                import base64
                # Metni byte'a çevir, base64 kodla, sonra tekrar string yap
                sonuc = base64.b64encode(ham_metin.encode()).decode()

        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.insert("1.0", sonuc)

if __name__ == "__main__":
    app = ctk.CTk()
    KriptoUygulamasi(app)
    app.mainloop()