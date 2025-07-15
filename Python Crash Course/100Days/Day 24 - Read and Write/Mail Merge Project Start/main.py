#TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt") as inv_names:
    name_arr = inv_names.read().split()
with open("./Input/Letters/starting_letter.txt") as st_ltr:
    temp_read = st_ltr.read()
    for name in name_arr:
        add_invitee = temp_read.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", 'w') as sent:
            sent.write(add_invitee)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp