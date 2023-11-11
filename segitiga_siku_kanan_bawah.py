jumlah = int(input('Masukan Tinggi Segitiga : '))
for i in range(jumlah):
    for j in range(jumlah - i - 1):
        print('  ', end=' ')
    for k in range(i + 1):
        print('*', end='  ')
    print()

