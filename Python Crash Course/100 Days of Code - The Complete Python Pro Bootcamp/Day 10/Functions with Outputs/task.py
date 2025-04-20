
def format_name(f_name="f_name", l_name="l_name"):
    f_name = input("What is your first name?:\n").title()
    l_name = input("What is your last name?:\n").title()
    return f"{f_name} {l_name}, are you here?"

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)


