email = input("Email manzilingizni kiriting: ")

if "@" in email and (email.endswith(".com") or email.endswith(".uz") or email.endswith(".net") or email.endswith(".org")):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")