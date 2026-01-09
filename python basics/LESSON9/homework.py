# def my_len(my_list):
#     son = 0
#     for _ in my_list:
#         son += 1
#     return son


# mevalar = ["olma", "banan", "shaftoli"]
# print(my_len(mevalar))

# mevalar = ["olma", "banan", "shaftoli"]
# uzunlik = len(mevalar)
# print(uzunlik)


# def my_sum(my_list):
#     yigindi = 0
#     for son in my_list: 
#         yigindi += son
#     return yigindi


# sonlar = [1, 2, 3, 4]
# print(my_sum(sonlar))


# sonlar = [1, 2, 3, 4]
# yigindi = sum(sonlar)
# print(yigindi) 


# def my_max(my_list):
#     if not my_list:  
#         return None
#     eng_katta = my_list[0]  
#     for son in my_list[1:]:  
#         if son > eng_katta:
#             eng_katta = son
#     return eng_katta


# sonlar = [5, 12, 3, 8]
# print(my_max(sonlar))






# sonlar = [5, 12, 3, 8]
# eng_katta = max(sonlar)
# print(eng_katta)  


# def my_min(my_list):
#     if not my_list: 
#         return None
#     eng_kichik = my_list[0]  
#     for son in my_list[1:]:  
#         if son < eng_kichik:
#             eng_kichik = son
#     return eng_kichik


# sonlar = [5, 12, 3, 8]
# print(my_min(sonlar))





# sonlar = [5, 12, 3, 8]
# eng_kichik = min(sonlar)
# print(eng_kichik)


# def hisoblovchi(ism, yosh):
#     yil=2026
#     hisob=yil-yosh
#     print(f"{ism } {hisob} yilda tug'ilgan ")
    
# ism=input("ismingiz")
# yosh = int(input("yoshingiz"))

# hisoblovchi(ism,yosh)


# def hisoblovchi(ism, yosh):
#     yil=2026
#     hisob=yil-yosh
#     print(f"{ism } {hisob} yilda tug'ilgan : ")
    
# ism= str(input("ismingiz : "))
# yosh = int(input("yoshingiz "))


# hisoblovchi(ism,yosh)

# def mat(son):
#     print(son**2)
#     print(son**3)

# son = int(input("son : "))
# mat(son)



# def hisob(son):
#     if son%2==0:
#         print("son juft")
#     else:
#         print("son toq")

# son = int(input("son : "))
# hisob(son)


# def kattak_kichik(son1,son2):
#     if son1>son2:
#         print(f"{son1} katta {son2} kichik")
#     elif son2>son1:
#         print(f"{son2} katta {son1} kichik")
#     else:
#         print("sonlar teng")

# son1 = int(input("1chi son "))
# son2 = int(input("2chi son "))

# kattak_kichik(son1,son2)


# def darajasi(x,n):
#     print(x**n)

# x=int(input("x ni kiriting : "))
# n =int(input("n ni kiriting : "))

# darajasi(x,n)


# def Qoldiq(son):
#     for n in sonlar:
#         if son % n ==0:
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{son} soni {n} ga qoldiq bilan bo'linadi")
    

# son = int(input("son : "))
# sonlar= []
# sonlar= list(range(2,11))

# Qoldiq(son,sonlar)

# def Qoldiq(son, sonlar):
#     for n in sonlar:
#         if son % n == 0:
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{son} soni {n} ga qoldiq bilan bo'linadi")

# son = int(input("son : "))
# sonlar = list(range(2, 11))
# Qoldiq(son, sonlar)