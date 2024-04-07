import time 

sleep_time = 1
x = input("Введите x:")
x = float(x)
print("Я записал в переменную x значение", x)
time.sleep(sleep_time)
print("Давайте теперь попробуем добавить к x 10")
time.sleep(sleep_time)
print("x + 10 =", x + 10)
print("Отлично! давайте теперь это значение запишем в переменную y")
time.sleep(sleep_time)
y = x + 10
print("Теперь выведем y")
print("y =", y)
time.sleep(sleep_time)
print("Теперь давайте проверим, что будет если привет добавить к", x)
time.sleep(sleep_time)
print("Запишем в x привет как строку")
# x = "привет"
# print("Теперь напишем x + 10")
# y = 10
# print(x + str(y))
print("x * 5 =", x * 5)
time.sleep(sleep_time)
print("x / 5 =", x / 5)
time.sleep(sleep_time)
print("x + 5 =", x + 5)
time.sleep(sleep_time)
print("x - 5 =", x - 5)
time.sleep(sleep_time)
print("x ** 5 =", x ** 5)
time.sleep(sleep_time)
print("x % 5 =", x % 5)
time.sleep(sleep_time)
print("x // 5 =", x // 5)

print("2 + 2 * 2 =", 2 + 2 * 2)
print("(2 + 2) * 2 =", (2 + 2) * 2)