def hitung_total_harga(barang, harga, jumlah):
    total_harga = sum(harga[i] * jumlah[i] for i in range(len(barang)))  # Menghitung total harga

    return total_harga

def cetak_struk(barang, harga, jumlah, total_harga):
    print("===== Struk Belanja =====")
    for i in range(len(barang)):
        print(f"{barang[i]} \t {harga[i]} \t x{jumlah[i]}")
    print("=========================")
    print(f"Total Harga: \t {total_harga}")

# Daftar barang dan harganya
barang = ["Roti", "Gula", "Susu", "Kopi"]
harga = [5000, 10000, 15000, 8000]

# Inisialisasi list jumlah barang yang dibeli
jumlah = [0] * len(barang)

# Memasukkan jumlah barang yang dibeli
for i in range(len(barang)):
    jumlah[i] = int(input(f"Masukkan jumlah {barang[i]} yang dibeli: "))

# Menghitung total harga
total_harga = hitung_total_harga(barang, harga, jumlah)

# Mencetak struk belanja
cetak_struk(barang, harga, jumlah, total_harga)