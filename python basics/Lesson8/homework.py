# otam = {'ism':'Ali','yili':1975,'shahri':'Toshkent','kasbi':'muhandis'}
# onam = {'ism':'Gulnoza','yili':1978,'shahri':'Samarqand','kasbi':'o\'qituvchi'}
# akam = {'ism':'Javohir','yili':1998,'shahri':'Toshkent','talimi':'student'}
# ukam = {'ism':'Shohruh','yili':2005,'shahri':'Toshkent','sinfi':9}

# print("Oila a'zolari:")
# print(f"Otam: {otam['ism']}, {otam['yili']}-yil, {otam['shahri']}, {otam['kasbi']}")
# print(f"Onam: {onam['ism']}, {onam['yili']}-yil, {onam['shahri']}, {onam['kasbi']}")
# print(f"Akam: {akam['ism']}, {akam['yili']}-yil, {akam['shahri']}, {akam['talimi']}")
# print(f"Ukam: {ukam['ism']}, {ukam['yili']}-yil, {ukam['shahri']}, {ukam['sinfi']}-sinf")


# oilam = [
#     {'kim': 'Otam', 'ism': 'Ali', 'yil': 1975, 'shahar': 'Toshkent', 'malumot': 'muhandis'},
#     {'kim': 'Onam', 'ism': 'Gulnoza', 'yil': 1978, 'shahar': 'Samarqand', 'malumot': "o'qituvchi"},
#     {'kim': 'Akam', 'ism': 'Javohir', 'yil': 1998, 'shahar': 'Toshkent', 'malumot': 'student'},
#     {'kim': 'Ukam', 'ism': 'Shohruh', 'yil': 2005, 'shahar': 'Toshkent', 'malumot': '9-sinf'}
# ]

# print("Oila a'zolari:")
# for azo in oilam:
#     print(f"{azo['kim']}: {azo['ism']}, {azo['yil']}-yil, {azo['shahar']}, {azo['malumot']}")


# s_taomlar ={
#     'hasan':'manti',
#     'zuhra':'honim',
#     'asad':'osh',
#     'malika':'shurva',
#     'zohid':"lag'mon"
# }

# for k , v in s_taomlar.items():
#     print(f"{k.title()}ning sevimli taomi {v}.")


# p_lugat = {
#     'integer':'butun son',
#     'float':'haqiqiy son',
#     'string':'matn',
#     'list':'ro\'yxat',
#     'tuple':'kortezh',
#     'dictionary':'lug\'at',
#     'boolean':'mantiqiy qiymat',
#     "lug'at":'dictionary'
# }


# izohli_lugat={
#         'integer':'butun son',
#     'float':'haqiqiy son',
#     'string':'matn',
#     'list':'ro\'yxat',
#     'tuple':'kortezh',
#     'dictionary':'lug\'at',
#     'boolean':'mantiqiy qiymat',
#     "lug'at":'dictionary'
# }

# for k , v in izohli_lugat.items():
#     print(f"{k} = {v}")


# restoran_menu ={
#         'osh':20000,
#         'shashlik':25000,
#         'lagmon':22000,
#         'somsa':12000,
#         'shorva':18000,
#         'norin':25000,
#         'mastava':20000,
#         'kabob':30000,
#         'chuchvara':15000
# }
# i=0
# while i<3:
#     buyurtma = input("Nima zakaz qilasiz: ")
#     if buyurtma=='exit':
#         break
#     elif buyurtma in restoran_menu:
#         print(f"{buyurtma.title()} narxi {restoran_menu[buyurtma]} so'm")
#     else:
#         print("Bizda bunday taom yo'q.")
#     i+=1
# shaxslar = [
#     {
#         'ism':'Lianrdo',
#         'familiya':'da Vinchi',
#         'tyil':1452,
#         'vyl':1519,
#         'kasb':'Rassom va ixtirochi'
#     },
#     {
#         'ism':'Albert',
#         'familiya':'Eynshteyn',
#         'tyil':1879,
#         'vyl':1955,
#         'kasb':'Fizik'
#     },
#     {
#         'ism':'Isaac',
#         'familiya':'Nyuton',
#         'tyil':1643,
#         'vyl':1727,
#         'kasb':'Matematik va fizik'
#     },
#     {
#         'ism':'Marie',
#         'familiya':'Kyuri',
#         'tyil':1867,
#         'vyl':1934,
#         'kasb':'Kimyogar'
#     }
# ]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism']} {shaxs['familiya']},"
#           f"{shaxs['tyil']}-yilda tug'ilgan,"
#           f"{shaxs['vyl']}-yilda vafot etgan,"
#           f"Kasbi: {shaxs['kasb']}.")
    
# shaxslar[0].update({'asari':'Monaliza'})
# shaxslar[1].update({'asari':'Nisbiylik nazariyasi'})
# shaxslar[2].update({'asari':'Matematikaning asoslari'})
# shaxslar[3].update({'asari':'Radioaktivlik'})
# for shaxs in shaxslar:
#     print(f"{shaxs['ism']} {shaxs['familiya']},"
#           f"{shaxs['tyil']}-yilda tug'ilgan,"
#           f"{shaxs['vyl']}-yilda vafot etgan,"
#           f"Kasbi: {shaxs['kasb']},"
#           f"Asari: {shaxs['asari']}.")


# print("Sevimli kitoblaringizni kiriting (to'xtash uchun 'stop' deb yozing):")

# kitoblar = []  

# while True:
#     kitob = input("> ").strip()
    
#     if kitob.lower() == "stop":
#         break
    
#     if kitob:
#         kitoblar.append(kitob)
#     else:
#         print("Iltimos, kitob nomini kiriting yoki 'stop' deb yozing.")

# print("\nSizning sevimli kitoblaringiz:")
# if kitoblar:
#     for i, kitob in enumerate(kitoblar, 1):
#         print(f"{i}. {kitob}")
# else:
#     print("Hech qanday kitob kiritilmadi.")

# print("\n\nMuzey chiptasi narxini hisoblash")
# print("Yoshingizni kiriting (dasturni to'xtash uchun 'exit' yoki 'stop' deb yozing)")

# while True:
#     javob = input("Yoshingiz: ").strip()
    
#     if javob.lower() in ["exit", "stop"]:
#         print("Dastur tugadi. Xayr!")
#         break
    
    
#     if not javob.isdigit():
#         print("Xato! Iltimos, faqat musbat butun son kiriting.")
#         continue
    
#     yosh = int(javob)

#     if yosh < 0:
#         print("Xato! Yosh manfiy bo'lishi mumkin emas.")
#         continue

#     if yosh <= 6 or yosh >= 65:
#         narx = 0
#         print(f"{yosh} yoshdagi uchun chipta bepul (0 so'm)")
#     elif 7 <= yosh <= 18:
#         narx = 3000
#         print(f"{yosh} yoshdagi uchun chipta narxi: {narx} so'm")
#     else:  
#         narx = 10000
#         print(f"{yosh} yoshdagi uchun chipta narxi: {narx} so'm")
    
#     print("-" * 40)








# buyurtmalar = []

# print("Buyurtma qiling (tayyor bo'lgach 'tayyor' deb yozing):")

# while True:
#     mahsulot = input("> ").strip()
    
#     if mahsulot.lower() == "tayyor":
#         break
    
#     if mahsulot:
#         buyurtmalar.append(mahsulot)

# e_bozor = {
#     "olma": 8000,
#     "banan": 12000,
#     "apelsin": 15000,
#     "uzum": 20000,
#     "anor": 18000,
#     "shaftoli": 10000,
#     "qovun": 25000,
#     "tarvuz": 30000,
#     "non": 3000,
#     "sut": 9000
# }

# print("\nBuyurtmangiz qabul qilindi. Narxlarni hisoblaymiz:\n")

# if not buyurtmalar:
#     print("Hech qanday mahsulot buyurtma qilinmadi.")
# else:
#     for mahsulot in buyurtmalar:
#         mahsulot_lower = mahsulot.lower()
#         if mahsulot_lower in e_bozor:
#             narx = e_bozor[mahsulot_lower]
#             print(f"{mahsulot.capitalize()} - {narx} so'm")
#         else:
#             print(f"{mahsulot.capitalize()} - Bizda bu mahsulot yo'q")

# print("\nBuyurtmangiz uchun rahmat!")






# son = float(input("Juft son kiriting: "))

# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas.")

# yosh = int(input("Yoshingiz nechida? "))

# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh <= 18:
#     narx = 10000
# else:
#     narx = 20000

# print(f"Chipta {narx} so'm")
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))

# if x == y:
#     print(f"{x}={y}")
# elif x < y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', 'yog\'', 'sovun', 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# if savat:
#     print("Savatingiz bo'sh")

# users = ['alisher1983', 'aziza', 'yasina', 'umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz!")





# x = int(input("son kiriting: "))
# y = int(input("yana bir son kiriting: "))

# try:
#     natija = x / y
#     print(x, '/', y, '=', natija)
# except ZeroDivisionError:
#     print("Xato: Nolga bo'lish mumkin emas!")



