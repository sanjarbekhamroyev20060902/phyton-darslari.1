'''
son = int (input(input("raqam k: ")))
if son > 7:
    print ("son 7 dan katta")
elif son < 5:
    print (" son 5 dan kichik")
elif son > 100:
    print ("son judda katta ")
else: print ("nimadir")
'''
'''
bolinadigan5 = []
for num in range(50):
    if num % 5 == 0:
        bolinadigan5.append (num)
        print(bolinadigan5)
        '''

'''
yigindi = 0
for son in range(5):
    yigindi += float (input(f"{son+1}-raqamni kiriting: "))
print(yigindi)
'''



yosh = int (input ("yoshingizni kiriting: "))
if yosh < 7: 
    narx = 20000
elif yosh < 18:
    narx = 10000
elif yosh < 65:
    narx = 50000
else:
    narx = 30000
    print (f"sizning chipta narxingiz {narx} so'm")

