# Циклы и операторы в них (for, while)
# Циклы - специальнеы конструкции, которые позволяют запускать код несколько раз подряд, количество выполнений указывается самостоятельно
# Существует 2 формата циклов: for  / while




######### for:   удобно использогвать, когда нужно сделать перебор

# for i in range(6):    # выведет числа от 0 до 5
#     print(i)
#
# for i in range(1, 6):  # выведет числа в интервале от 1 до 6: 1 - начальное значение, 6 - конечное значение (начально значение можно не писать, тогда счет будет с 0 (см. код наверху))
#     print(i)

# for i in range(1, 6, 2):  # выведет числа в интервале от 1 до 6 с шагом 2: результат = 1, 3, 5 (2 - это шаг)
#     print(i)






####### поиск определенного символа в строке (перебор строки):
# count = 0
# word = "Monti"
# for i in word:
#     if i == "!":
#         continue
#     if i == "M":
#         count += 1
# print("Number of letters:", count)  # вывод количества найденных букв в слове

    # else:
    #     print("False")
    # else:
    #     print("False")






############ while:
# отличается от for только форматом записи, удобен тем, что можно просто прописать условие, и пока оно будет истинным, цикл будет работать

# a = 5
# while a < 10: #цикл будет длиться до тех пор, пока "a" не примет значение больше 10
#     print(a)
#     a += 2

# isHasCar = True
# while isHasCar:
#     if input("Enter data") == "Stop":
#         isHasCar = False






########### операторы в циклах:              break / continue
# for i in range(1, 11):
#     if i == 5:
#         break  #break - завершает цикл при определенном условии if
#     if i % 2 == 0:
#         continue
#     print(i)







# name = "Anna"
# for i in name:
#     if i == "A":
#         print("A")
#     if i == "n":
#         print("n")
#     if i == "a":
#         print("a")







# found = None
# for i in ["Anna"]:                  # [] - перебор списка символов из одной строки
#     if i == "Anna":
#         found = True
#         break
# else:
#     found = False
# print(found)


# или

found = "Anna" in "Anna"
print(found)                     # True


#конец урока