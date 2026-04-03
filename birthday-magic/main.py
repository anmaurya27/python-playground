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
      "\nMultiply that number by 2.")
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
      "\nNow for the final step, add the date you were born on.")
input("press enter for next step_")

final_answer = int(input("\nNow tell me the final answer = "))
sub = final_answer - 250

sub_str = str(sub)
length_of_sub = len(sub_str)
month_name = "0"

if length_of_sub == 4:
    month = sub_str[0] + sub_str[1]
    if month == "10":
        month_name = "October"
    elif month == "11":
        month_name = "November"
    else:
        month_name = "December"
else:
    month = sub_str[0]
    if month == "1":
        month_name = "January"
    elif month == "2":
        month_name = "February"
    elif month == "3":
        month_name = "March"
    elif month == "4":
        month_name = "April"
    elif month == "5":
        month_name = "May"
    elif month == "6":
        month_name = "June"
    elif month == "7":
        month_name = "July"
    elif month == "8":
        month_name = "August"
    else:
        month_name = "Spetember"

day = sub_str[-2] + sub_str[-1]
print(f"You were born on {day} {month_name}")


# Python Concepts Used / Practised:
# - print() function
# - input() function
# - Variables
# - Type casting, str(), int()
# - String concatenation, +
# - Arithmetic operator (-)
# - Line break, \n
# - Subscripting: indexing
# - Condititonal statement: if, elif, else
# - length() function
# - Comparison operator, ==
