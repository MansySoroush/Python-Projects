PLACE_HOLDER = "[name]"

# Read template letter
with open("../Input/Letters/starting_letter.txt", "r") as starting_letter_file:
    content = starting_letter_file.read()

# For each name in invited_names.txt
with open("../Input/Names/invited_names.txt", "r") as file_names:
    names = file_names.readlines()

    # Replace the [name] placeholder with the actual name.
    for name in names:
        name = name.strip('\n')
        invited_content = content
        invited_content = invited_content.replace(PLACE_HOLDER, name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"./ReadyToSend/{name}.txt", "w") as file_invited:
            file_invited.write(invited_content)
