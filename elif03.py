soat = int(input("Soatni kiriting (0-23): "))

if soat < 0 or soat > 23:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")
elif 5 <= soat <= 11:
    print("Ertalab")
elif 12 <= soat <= 17:
    print("Kunduzi")
elif 18 <= soat <= 21:
    print("Kechqurun")
else:
    # 22-23 va 0-4 oralig'i uchun
    print("Tun")