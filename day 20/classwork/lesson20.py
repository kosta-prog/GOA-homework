num = 15
num2 = int(input("put a random number:"))
if num2 > num:
    print("the number is bigger than 15")
if not num2 > num:
    print("the number is smaller than 15")
if num2 == num:
    print("the number is equal to 15")

age = 5
age1 = int(input("შეიტანე შენი ასაკი აქ: "))
if age1 > age:
    print("გოაში შემოგვიერთდი")
elif age1 < age:
    print("ზედმეტად პატარა ხარ")
elif age1 > 15:
    print("აქამდე რატო არ შემოუერთდი გოას?")
else:
    print("გოაში შემოგვიერთდი")