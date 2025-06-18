masofa = float(input("Masofani kiriting (km): "))

if masofa < 0:
    print("Masofa manfiy bo'la olmaydi!")
elif 0 <= masofa <= 1:
    print("Piyoda yuring")
elif 1 < masofa <= 5:
    print("Velosiped yoki elektr skuter")
elif 5 < masofa <= 50:
    print("Avtobus yoki mashina")
else:
    # 50 dan katta masofa uchun
    print("Poyezd yoki samolyot")