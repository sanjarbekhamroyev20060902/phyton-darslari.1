def funksiya(): 
    otam = {'ism':'Ali','yili':1975,'shahri':'Toshkent','kasbi':'muhandis'}
    onam = {'ism':'Gulnoza','yili':1978,'shahri':'Samarqand','kasbi':'o\'qituvchi'}
    akam = {'ism':'Javohir','yili':1998,'shahri':'Toshkent','talimi':'student'}
    ukam = {'ism':'Shohruh','yili':2005,'shahri':'Toshkent','sinfi':9}

    print("Oila a'zolari:")
    print(f"Otam: {otam['ism']}, {otam['yili']}-yil, {otam['shahri']}, {otam['kasbi']}")
    print(f"Onam: {onam['ism']}, {onam['yili']}-yil, {onam['shahri']}, {onam['kasbi']}")
    print(f"Akam: {akam['ism']}, {akam['yili']}-yil, {akam['shahri']}, {akam['talimi']}")
    print(f"Ukam: {ukam['ism']}, {ukam['yili']}-yil, {ukam['shahri']}, {ukam['sinfi']}-sinf")

# funksiya()


def funksiya1():
    oilam = [
    {'kim': 'Otam', 'ism': 'Ali', 'yil': 1975, 'shahar': 'Toshkent', 'malumot': 'muhandis'},
    {'kim': 'Onam', 'ism': 'Gulnoza', 'yil': 1978, 'shahar': 'Samarqand', 'malumot': "o'qituvchi"},
    {'kim': 'Akam', 'ism': 'Javohir', 'yil': 1998, 'shahar': 'Toshkent', 'malumot': 'student'},
    {'kim': 'Ukam', 'ism': 'Shohruh', 'yil': 2005, 'shahar': 'Toshkent', 'malumot': '9-sinf'}
]

    print("Oila a'zolari:")
    for azo in oilam:
        print(f"{azo['kim']}: {azo['ism']}, {azo['yil']}-yil, {azo['shahar']}, {azo['malumot']}")

# funksiya1()


def funksiya2():
    s_taomlar ={
    'hasan':'manti',
    'zuhra':'honim',
    'asad':'osh',
    'malika':'shurva',
    'zohid':"lag'mon"
    }

    for k , v in s_taomlar.items():
      print(f"{k.title()}ning sevimli taomi {v}.")


# funksiya2()

def funksiya3():
    p_lugat = {
    'integer':'butun son',
    'float':'haqiqiy son',
    'string':'matn',
    'list':'ro\'yxat',
    'tuple':'kortezh',
    'dictionary':'lug\'at',
    'boolean':'mantiqiy qiymat',
    "lug'at":'dictionary'
     }


    izohli_lugat={
        'integer':'butun son',
    'float':'haqiqiy son',
    'string':'matn',
    'list':'ro\'yxat',
    'tuple':'kortezh',
    'dictionary':'lug\'at',
    'boolean':'mantiqiy qiymat',
    "lug'at":'dictionary'
     }

    for k , v in izohli_lugat.items():
       print(f"{k} = {v}")

# funksiya3()

def funksiya4():
        restoran_menu ={
        'osh':20000,
        'shashlik':25000,
        'lagmon':22000,
        'somsa':12000,
        'shorva':18000,
        'norin':25000,
        'mastava':20000,
        'kabob':30000,
        'chuchvara':15000
        }
        i=0
        while i<3:
            buyurtma = input("Nima zakaz qilasiz: ")
        if buyurtma=='exit':
         break
        elif buyurtma in restoran_menu:
         print(f"{buyurtma.title()} narxi {restoran_menu[buyurtma]} so'm")
        else:
             print("Bizda bunday taom yo'q.")
        i+=1
        shaxslar = [
            {
            'ism':'Lianrdo',
            'familiya':'da Vinchi',
            'tyil':1452,
            'vyl':1519,
            'kasb':'Rassom va ixtirochi'
            },
            {
            'ism':'Albert',
            'familiya':'Eynshteyn',
            'tyil':1879,
            'vyl':1955,
            'kasb':'Fizik'
            },
            {
            'ism':'Isaac',
            'familiya':'Nyuton',
            'tyil':1643,
            'vyl':1727,
            'kasb':'Matematik va fizik'
            },
            {
            'ism':'Marie',
            'familiya':'Kyuri',
            'tyil':1867,
            'vyl':1934,
            'kasb':'Kimyogar'
            }
            ]
        
        for shaxs in shaxslar:
            print(f"{shaxs['ism']} {shaxs['familiya']},"
        f"{shaxs['tyil']}-yilda tug'ilgan,"
        f"{shaxs['vyl']}-yilda vafot etgan,"
        f"Kasbi: {shaxs['kasb']}.")
            
        shaxslar[0].update({'asari':'Monaliza'})
        shaxslar[1].update({'asari':'Nisbiylik nazariyasi'})
        shaxslar[2].update({'asari':'Matematikaning asoslari'})
        shaxslar[3].update({'asari':'Radioaktivlik'})
        for shaxs in shaxslar:
            print(f"{shaxs['ism']} {shaxs['familiya']},"
        f"{shaxs['tyil']}-yilda tug'ilgan,"
        f"{shaxs['vyl']}-yilda vafot etgan,"
        f"Kasbi: {shaxs['kasb']},"
        f"Asari: {shaxs['asari']}.")
            print("Sevimli kitoblaringizni kiriting (to'xtash uchun 'stop' deb yozing):")    
            
funksiya4()