import os

fayl_nomi = input("Fayl nomini kiriting: ")

if os.path.exists(fayl_nomi):
    print(f"Fayl '{fayl_nomi}' mavjud.")
else:
    print(f"Fayl '{fayl_nomi}' topilmadi.")