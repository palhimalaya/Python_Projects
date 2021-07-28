PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        print(striped_name)
        new_letter = letter_content.replace(PLACEHOLDER,striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
