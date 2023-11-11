tinggi = int(input("Masukkan tinggi piramida: "))
i = 1
while i <= tinggi:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1