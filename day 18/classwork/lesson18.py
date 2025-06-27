for i in range(1,20):
    print(i)

for i in range(1,20,2):
    print(i)

# For ციკლს ვიყენებთ, როდესაც ვიცით კოდი რამდენჯერ გვინდა გავუშვათ, ხოლო while ციკლს ვიყენებთ,
# როდესაც არ ვიცით

random_number = int(input('please enter a number: 1-20'))

while random_number == 30:
    random_number = random_number + 1

number = 15
for i in range(15):
    number = number + 1
number = input('ss')
counter = 15
while counter <= 20:
    print(counter)
    counter = counter + 1


#1 savarjisho

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Total sum is:", sum)

#2 savarjisho

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        sum = sum + i

print("Sum of odd numbers is:", sum)

#savarjisho 3

password = int(input("Enter your password: "))
password_numbers = password
comfirm_password = int(input("Confirm your password: "))
while password_numbers != comfirm_password:
    print("Passwords do not match, please try again.")
    comfirm_password = int(input("Confirm your password: "))
if password_numbers == comfirm_password:
    print("Password confirmed successfully.")

# savarjisho 4

i = 1

while i <= 100:
    print(i)
    i = i + 2
