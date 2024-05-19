# tulis solusi code disini
import math

class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def volume(self):
        return math.pi * (self.jari_jari ** 2) * self.tinggi

def main():
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)

    print(f"Volume Kubus : {kubus.volume()}")
    print(f"Volume Balok : {balok.volume()}")
    print(f"Volume Tabung : {tabung.volume():.0f}")

if __name__ == "__main__":
    main()
 