#Project: Birthday Magic

print("Welcome to Birthday Magic !!!")
print("\nI can know your, your birth month and birth day without you telling me."
      "\nYou just need to do some calculations as I say, step-by-step.")
input("If you are ready press enter_")

print("\nStep 1:"
      "\nThink of the month you were born in and keep that number in mind."
      "\nExample- If your birthday is in March, then keep 3 in your mind.")
input("press enter for next step_")

print("\nStep 2:"
      "\nMultiply the number by 2.")
input("press enter for next step_")

print("\nStep 3:"
      "\nNow add 5")
input("press enter for next step_")

print("\nStep 4:"
      "\nThen multiply again by 5")
input("Still following? then press enter for next step_")

print("\nStep 5:"
      "\nNow you have to put a zero after the number you have in your mind."
      "\nExample- If your number is 45 the add zero at the end it will become 450.")
input("press enter for next step_")

print("\nStep 6:"
      "\nNow for the final step, add the date you were born to the answer from step 5.")
input("press enter for next step_")

final_number = int(input("\nNow tell me the final answer = "))
result = final_number - 250
print(f"\nSo your month and date of birth is: {result}")
print("The last two digits are your Birth date & the remaining digits are you Birth month.")


# Python Concepts Used / Practised:
# - print() function
# - input() function
# - line break, \n
# - Variables
# - Arithmetic operators [-]
# - Type casting, int()
# - f String

