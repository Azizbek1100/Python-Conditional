vazn = float(input("Vazningizni kiriting (kg): "))
boy = float(input("Bo'yingizni kiriting (m): "))

# Qo'shimcha tekshiruvlar
if vazn < 1 or vazn > 500:
    print("Vazn 1 dan 500 kg gacha bo'lishi kerak.")
elif boy < 0.5 or boy > 3.0:
    print("Bo'y 0.5 dan 3.0 metr oralig'ida bo'lishi kerak.")
elif vazn > 0 and boy > 0:
    bmi = vazn / (boy ** 2)
    print(f"BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Tasnif: Kam vazn")
    elif 18.5 <= bmi < 25:
        print("Tasnif: Normal vazn")
    elif 25 <= bmi < 30:
        print("Tasnif: Ortiqcha vazn")
    else:
        print("Tasnif: Semizlik")
else:
    print("Vazn va bo'y musbat bo'lishi kerak.")