print("==== Menghitung Nilai Rata-Rata ====")

total_nilai = []
jumlah_nilai = int(input('Masukkan jumlah nilai : '))

i = 1
while i <= jumlah_nilai:
    nilai = float(input("Masukkan Nilai : "))
    total_nilai.append(nilai)
    i = i + 1

#menghitung rata-rata
rata_rata = sum(total_nilai)/jumlah_nilai
print("Nilai Rata-Rata Anda Adalah : ", rata_rata)