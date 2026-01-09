# lugat = {
#     "print": "konsolga chiqarish",
#     "if": "shart operatori",
#     "else": "aks holda",
#     "for": "takrorlash sikli",
#     "while": "shartli sikl",
#     "list": "ro‘yxat",
#     "tuple": "o‘zgarmas ro‘yxat",
#     "dict": "lug‘at",
#     "set": "takrorlanmas to‘plam",
#     "int": "butun son"
# }

# for kalit in sorted(lugat):
#     print(f"{kalit} — {lugat[kalit]}")

# davlatlar = {
#     "O‘zbekiston": "Toshkent",
#     "AQSH": "Vashington",
#     "Rossiya": "Moskva",
#     "Fransiya": "Parij",
#     "Yaponiya": "Tokio"
# }

# print("Davlatlar:")
# for d in sorted(davlatlar):
#     print(d)

# print("\nPoytaxtlar:")
# for p in sorted(davlatlar.values()):
#     print(p)

# davlat = input("Davlat nomini kiriting: ")

# if davlat in davlatlar:
#     print(f"{davlat} poytaxti — {davlatlar[davlat]}")
# else:
#     print("Bizda bunday ma'lumot yo‘q")


# shaxslar = [
#     {
#         "ism": "Alisher Navoiy",
#         "soha": "adabiyot",
#         "yil": 1441,
#         "asarlar": ["Xamsa", "Lison ut-tayr"]
#     },
#     {
#         "ism": "Albert Einstein",
#         "soha": "ilm-fan",
#         "yil": 1879,
#         "asarlar": ["Nisbiylik nazariyasi"]
#     },
#     {
#         "ism": "Leonardo da Vinci",
#         "soha": "san’at",
#         "yil": 1452,
#         "asarlar": ["Mona Liza"]
#     },
#     {
#         "ism": "Bill Gates",
#         "soha": "internet",
#         "yil": 1955,
#         "asarlar": ["Microsoft"]
#     }
# ]

# for shaxs in shaxslar:
#     print(f"\nIsm: {shaxs['ism']}")
#     print("Asarlari:")
#     for asar in shaxs["asarlar"]:
#         print("-", asar)

# kino_lugat = {}

# for i in range(3):
#     ism = input("Do‘stingiz ismi: ")
#     kinolar = input("Sevimli kinolari (vergul bilan): ").split(",")
#     kino_lugat[ism] = kinolar

# for ism, kinolar in kino_lugat.items():
#     print(f"\n{ism} ning sevimli kinolari:")
#     for kino in kinolar:
#         print("-", kino.strip())

# davlatlar_info = {
#     "O‘zbekiston": {
#         "poytaxt": "Toshkent",
#         "aholi": "36 mln",
#         "til": "O‘zbek"
#     },
#     "Yaponiya": {
#         "poytaxt": "Tokio",
#         "aholi": "125 mln",
#         "til": "Yapon"
#     }
# }

# davlat = input("Davlat nomini kiriting: ")

# if davlat in davlatlar_info:
#     info = davlatlar_info[davlat]
#     for k, v in info.items():
#         print(f"{k}: {v}")
# else:
#     print("Bizda bu davlat haqida ma'lumot yo‘q")


# 116-betdagi pastdagilar 

# 1-vazifa: Internet olamidagi 4 ta mashhur shaxs haqida lug'atlar ro'yxati


# shaxslar = [
#     {
#         'ism': 'Elon Musk',
#         'kasb': 'Tadbirkor, muhandis',
#         'tugilgan_yil': 1971,
#         'tugilgan_joy': 'Janubiy Afrika',
#         'asarlar': ['Tesla avtomobillari', 'SpaceX raketalari', 'Neuralink', 'The Boring Company']
#     },
#     {
#         'ism': 'Bill Gates',
#         'kasb': 'Dasturchi, tadbirkor',
#         'tugilgan_yil': 1955,
#         'tugilgan_joy': 'AQSh',
#         'asarlar': ['Microsoft Windows', 'Microsoft Office', 'Kitob: The Road Ahead']
#     },
#     {
#         'ism': 'Tim Berners-Lee',
#         'kasb': 'Ilmiy xodim, WWW ixtirochisi',
#         'tugilgan_yil': 1955,
#         'tugilgan_joy': 'Angliya',
#         'asarlar': ['World Wide Web', 'HTML', 'HTTP']
#     },
#     {
#         'ism': 'Linus Torvalds',
#         'kasb': 'Dasturchi',
#         'tugilgan_yil': 1969,
#         'tugilgan_joy': 'Finlyandiya',
#         'asarlar': ['Linux yadrosi', 'Git']
#     }
# ]

# print("1-vazifa: Mashhur shaxslar va ularning asarlari")
# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism']} ({shaxs['kasb']})")
#     print("Mashhur asarlari:")
#     for asar in shaxs['asarlar']:
#         print(f"  - {asar}")

# # 2-vazifa: Do'stlarning sevimli kinolari (misol uchun 3 ta)
# sevimli_kinolar = {
#     'Ali': ['Inception', 'The Matrix', 'Interstellar'],
#     'Vali': ['The Godfather', 'Pulp Fiction', 'Fight Club'],
#     'Sardor': ['Lord of the Rings', 'Harry Potter', 'Avatar']
# }

# print("\n2-vazifa: Do'stlarning sevimli kinolari")
# for ism, kinolar in sevimli_kinolar.items():
#     print(f"\n{ism}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(f"  - {kino}")

# # 3-vazifa: Davlatlar haqida lug'at
# davlatlar = {
#     "O'zbekiston": {
#         'poytaxt': 'Toshkent',
#         'hudud': "448,978 km²",
#         'aholi': '35 million',
#         'pul birligi': 'so\'m'
#     },
#     "AQSh": {
#         'poytaxt': 'Vashington',
#         'hudud': "9,833,520 km²",
#         'aholi': '331 million',
#         'pul birligi': 'dollar'
#     },
#     "Rossiya": {
#         'poytaxt': 'Moskva',
#         'hudud': "17,098,246 km²",
#         'aholi': '144 million',
#         'pul birligi': 'rubl'
#     },
#     "Yaponiya": {
#         'poytaxt': 'Tokio',
#         'hudud': "377,975 km²",
#         'aholi': '125 million',
#         'pul birligi': 'iyena'
#     }
# }

# print("\n3-vazifa: Barcha davlatlar haqida ma'lumot")
# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.upper()}:")
#     print(f"  Poytaxt: {info['poytaxt']}")
#     print(f"  Hudud: {info['hudud']}")
#     print(f"  Aholi: {info['aholi']}")
#     print(f"  Pul birligi: {info['pul birligi']}")

# # 4-vazifa: Foydalanuvchi so'ragan davlat haqida ma'lumot
# print("\n4-vazifa: Davlat haqida ma'lumot olish")
# davlat_nomi = input("Davlat nomini kiriting: ").strip()

# if davlat_nomi in davlatlar:
#     info = davlatlar[davlat_nomi]
#     print(f"\n{davlat_nomi.upper()}:")
#     print(f"  Poytaxt: {info['poytaxt']}")
#     print(f"  Hudud: {info['hudud']}")
#     print(f"  Aholi: {info['aholi']}")
#     print(f"  Pul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q")

