# a = 7
# b = 7
# if a >= b:
#     print ("A")
# else:
#     print ("d")


# yosh = 40
# print (yosh !=7)

# if not(yosh <= 7 or yosh > 65):
#     print ("bepul")
# else:
#     print ("pullik")

#     numbers = []
#     for number in range (1, 11):
#         numbers.append (number)
#         print( numbers)


# n = 5
# num_str = ''
# FOR A IN range (1, n+1):
# print (f"{a}")
# pass 
# num_str +=str(a)
# print( num_str)
# ismlar = ['ali', 'vali', 'hasan', 'husan', 'olim' , "karim"]
# for ism in ismlar[1:4]:







import random
kom_num = random.randint (1, 10)
print (kom_num)
n = 1
while n < 6:
    user_guess = int (input (f"{n}-taxmin raqamingizni kiriting: "))
    if user_guess < kom_num:
        print (f" {n}- urunishda topdingiz va {(6-n)*10} ball oldingiz!")
        print ("Siz yuttiz!!!")
        break
    n += 1