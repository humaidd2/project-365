#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as data:
    unfiltered_names = data.readlines()
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


for name in unfiltered_names:
    name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        letter = starting_letter.readlines()
    text = ""
    for i in letter:
        text += i
    final_letter = text.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as content:
        content.write(final_letter)

