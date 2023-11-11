total_belanja = float(input("Total belanja: "))
if total_belanja >= 100000:
    diskon = total_belanja * 0.1
else:
    diskon = 0
print("Diskon yang Anda dapatkan: Rp", diskon)