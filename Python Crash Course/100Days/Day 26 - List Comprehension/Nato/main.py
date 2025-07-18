from Nato import Nato
def name_to_nato(times_run):

    if times_run == 0:
        # clear the file
        with open("nato_log.txt", mode="w") as file:
            file.write("")

    # Stop condition
    if times_run == 5:
        return

    enter_name = str(input("Please enter your name: "))
    nato_alpha = Nato()
    nato_list = [nato_alpha.nato_alphabet[letter.upper()] for letter in enter_name]

    with open("nato_log.txt", mode="a") as file:
        file.write(f"{enter_name}: ")
        for classification in nato_list:
            file.write(f"{classification} ")
        file.write("\n" * 2)
    times_run += 1
    name_to_nato(times_run)

name_to_nato(0)

