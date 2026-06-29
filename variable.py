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
print(word, str(digit + float(number)), sep=' ') # Приведение значения данных  нужному типу: str(), float(), int(), bool()
word = '1' #string
print(word + str(digit + float(number)))
# input("")
# input("")
