yosh = int(input("Yoshingizni kiriting: "))
narx = 100  # chipta narxi

if yosh < 7:
    narx = narx * 0.5  # 50% chegirma
if yosh >= 7 and yosh <= 17:
    narx = narx * 0.8  # 20% chegirma
if yosh > 60:
    narx = narx * 0.7  # 30% chegirma

print("Yakuniy narx:", narx, "so'm")