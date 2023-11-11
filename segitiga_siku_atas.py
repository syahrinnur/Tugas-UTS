jumlah = int(input("Masukan Tinggi Segitiga :"))
for i in range(jumlah, 0, -1):
    for j in range(i):
        print('*', end='  ')
    print()