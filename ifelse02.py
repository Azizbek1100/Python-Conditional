parol = input("Parol kiriting: ")

# 1-shart: uzunligi 8 dan kam bo'lmasligi
if len(parol) < 8:
    print("Parol juda qisqa! Kamida 8 ta belgidan iborat bo‘lishi kerak.")

# 2-shart: kamida 1 harf borligi
if not any(char.isalpha() for char in parol):
    print("Parolda kamida 1 ta harf bo‘lishi kerak.")

# 3-shart: kamida 1 raqam borligi
if not any(char.isdigit() for char in parol):
    print("Parolda kamida 1 ta raqam bo‘lishi kerak.")