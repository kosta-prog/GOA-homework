sum = 0
for i in range(1, 101):  # 1-დან 100-მდე (101 არ შედის)
    sum += i
print("ჯამი 1-დან 100-მდეა:", sum)

i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1

sum = 0
for i in range(10):
    number = int(input(f"{i+1}) შეიყვანე რიცხვი: "))
    sum += number
print("შეყვანილი რიცხვების ჯამი:", sum)

import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input(" გამოიცანი რიცხვი 1-დან 10-მდე: "))
    if guess != secret_number:
        print("არასწორია, სცადე ხელახლა!")

print("სწორია! სწორად გამოიცანი:", secret_number)
