balans = 5000
summasi = int(input("Yechmoqchi bo'lgan summani kiriting: "))

if summasi < 0:
    print("Manfiy summa kiritib bo'lmaydi.")
elif summasi <= balans:
    balans -= summasi
    print(f"Pul yechildi. Qolgan balans: {balans} so'm")
else:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")