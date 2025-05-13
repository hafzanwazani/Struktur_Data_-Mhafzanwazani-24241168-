print("=== Kalkulator Sederhana ===")
print("Masukkan dua angka dan pilih operasi (+, -, *, /)")

operasi = input("Masukkan operasi (+, -, *, /): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    hasil = angka1 + angka2
    print("Hasil:", hasil)
elif operasi == "-":
    hasil = angka1 - angka2
    print("Hasil:", hasil)
elif operasi == "*":
    hasil = angka1 * angka2
    print("Hasil:", hasil)
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil:", hasil)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operasi tidak valid. Silakan pilih +, -, *, atau /.")