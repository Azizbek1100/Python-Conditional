# Foydalanuvchidan ikkita son va amalni so'rash
son1 = float(input("1-son: "))
son2 = float(input("2-son: "))
amal = input("Amal (+, -, *, /): ")

if amal == '+':
    natija = son1 + son2
    print(f"Natija: {son1} + {son2} = {natija}")
elif amal == '-':
    natija = son1 - son2
    print(f"Natija: {son1} - {son2} = {natija}")
elif amal == '*':
    natija = son1 * son2
    print(f"Natija: {son1} * {son2} = {natija}")
elif amal == '/':
    if son2 == 0:
        print("Nolga bo'lish mumkin emas!")
    else:
        natija = son1 / son2
        print(f"Natija: {son1} / {son2} = {natija}")
else:
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")