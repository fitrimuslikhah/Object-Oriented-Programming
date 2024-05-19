# tulis solusi code disini
class Pengiriman:
    def hitung_harga(self, panjang, lebar, tinggi, berat):
        volume = panjang * lebar * tinggi
        berat_pcs = berat * 1000  # kg to grm

        if volume < 50 or berat_pcs < 1000:
            return 5000
        else:
            return 10000  

def main():
    pengiriman = Pengiriman()

    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1

    harga = pengiriman.hitung_harga(panjang, lebar, tinggi, berat)
    print(f"Harga : Rp {harga}")

if __name__ == "__main__":
    main()
