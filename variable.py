number = 5 #int
digit = 0.5 #float
word = 'one' #string
boolean1 = True #bool (1)
boolean2 = False #bool (0)
#
# del number # Удалить переменную

# print(number + digit)
# # print(word + number) - не отработает
# # print(word + boolean1) - не отработает
# print(boolean1 + boolean2)
# print(word * number)
#
# print(f"Result {number}") # Использование функциональной (f) строки. Тривиально: print("Result", number)
#
#print(word, str(digit + float(number)), sep=' ') # Приведение значения данных  нужному типу: str(), float(), int(), bool()
# word = '1' #string
# print(word + str(digit + float(number)))

# num1 = int(input("Введите число:"))
# num2 = int(input("Введите число:"))
#
# result = num1 + 5
# num2 += 9
# num1 -= num2
# print(result)
# print(num2)
# print(num1)
#
# word = "kaka"
# print(word, (word * 3), sep=' ')
# print(f"result {word * 5}")

a = 4
print(a / True) # True = 1, False = 0
print(a / False)