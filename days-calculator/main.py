# import helper # don't need all of helper module
from helper import validate_and_execute, user_input_message # Can also do from helper import, this way don't have to refernce module on each function called like the above.

# calling functions -------------------------------------------------
user_input = "" # input format= days:unit e.g. 10:hours or 20:minutes
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)  # don't need module. to reference function as we imported the function directly from the module