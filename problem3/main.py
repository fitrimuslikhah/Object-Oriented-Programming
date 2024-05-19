# tulis solusi code disini
import math

class Calculator:
    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

    def perkalian(self, a, b):
        return a * b

    def pembagian(self, a, b):
        if b == 0:
            return " "
        else:
            return a / b

def main():
    calc = Calculator()

    hasil_penjumlahan = calc.penjumlahan(3, 4)
    print(f"Penjumlahan : {hasil_penjumlahan}")

    hasil_pengurangan = calc.pengurangan(15, 4)
    print(f"Pengurangan : {hasil_pengurangan}")

    hasil_perkalian = calc.perkalian(10, 10)
    print(f"Perkalian : {hasil_perkalian}")

    hasil_pembagian = calc.pembagian(12, 3)
    print(f"Pembagian : {hasil_pembagian}")

if __name__ == "__main__":
    main()
