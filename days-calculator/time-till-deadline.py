from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon. e.g. goal:dd/mm/yyyy\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)

deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y") # converting input date into python module datetime format
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days")