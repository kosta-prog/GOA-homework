age = int(input("enter your age: "))
experience = int(input("enter your experience: "))
height = int(input("enter your height: "))
if age >= 15 and experience >= 1 and height >= 160:
    print("You are eligible to apply for the job.")
if not (age >= 15 and experience >= 1 and height >= 160):
    print("You are not eligible to apply for the job.")

people = int(input("put the number of humans: "))
hour = int(input("put the time (1 to 12): "))
switch = input("is it on? (true/false): ").lower() == 'true'

lightsOn = people > 2 and hour >= 7 and switch

print("lightsOn:", lightsOn)