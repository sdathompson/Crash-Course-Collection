def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

bool_leap = True

def is_leap_year(year):
    if year % 4 == 0 and not year % 100 == 0:
        return bool_leap
    elif year % 100 == 0 and year % 400 == 0:
        return bool_leap
    else:
        return bool_leap == False

leap_year = is_leap_year(int(input("Please enter a year:\n")))
print(leap_year)