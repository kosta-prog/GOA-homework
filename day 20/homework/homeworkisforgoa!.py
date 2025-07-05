# Variable to store the sum
total = 0

# Infinite loop to take numbers from the user
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    
    if num == 0:
        break  # Exit the loop if input is 0
    
    total += num  # Add the number to the total

# Print the final sum
print("The sum of the entered numbers is:", total)

week = int(input("Enter the week number: "))
if week == 1:
    print("კვირის დასაწყი")
elif week == 2 or week == 3 or week == 4:
    print("შუა კვირა")
elif week == 5:
    print("შაბათ-კვირას ახლოს")
elif week == 6 or week == 7:
    print("შაბათ-კვირა!")
elif week > 7:
    print("არასწორი დღეა")
    
# Ask the user to enter a word
word = input("Enter a word: ")

# List of Georgian vowels
vowels = "aeiouAEIOU"

# Counter for vowels
count = 0

# Loop through each letter in the word
for letter in word:
    if letter in vowels:
        count += 1

# Print the result
print("Number of vowels:", count)
