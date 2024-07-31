import csv

with open("./data/weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


import pandas

# Read from file
data = pandas.read_csv("./data/weather_data.csv")
temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)
print(average)

max_ = data["temp"].max()
print(max_)


# Get the column
print(data.condition)

# Get the row --> filtering data rows
print(data[data.day == "Monday"])
print(data[data.condition == "Sunny"])
print(data[data.temp == data.temp.max()])

# Get just temp columns with condition of sunny
sunny_rows = data[data.condition == "Sunny"]
print(sunny_rows["temp"])

monday = data[data.day == "Monday"]
degree_c = monday["temp"].values[0]
degree_f = degree_c * 1.8 + 32
print(degree_f)

# Make data frame from dictionary & Write it to file
my_dict = {
    "Name": ["Ali", "Mina", "Siamak", "Mansy"],
    "Score": [34, 22, 45, 65],
}
_new_data = pandas.DataFrame(my_dict)
_new_data.to_csv("./data/new_data.csv")


data = pandas.read_csv("./data/2018_Central_Park_Squirrel.csv")

gray_rows = data[data["Primary Fur Color"] == "Gray"]
gray_rows_count = gray_rows["Primary Fur Color"].count()

cinnamon_rows = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_rows_count = cinnamon_rows["Primary Fur Color"].count()

black_rows = data[data["Primary Fur Color"] == "Black"]
blck_rows_count = black_rows["Primary Fur Color"].count()

fur_color_dict = {
    "Primary Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [gray_rows_count, cinnamon_rows_count, blck_rows_count]
}

new_data = pandas.DataFrame(fur_color_dict)
new_data.to_csv("./data/2018_Central_Park_Squirrel_Fur_Color_Counts.csv")


# Loop through dictionary
my_dict = {
    "Name": ["Ali", "Mina", "Siamak", "Mansy"],
    "Score": [34, 22, 45, 65],
}

for (k, v) in my_dict.items():
    print(k)
    print(v)


# loop through a data frame
my_data_frame = pandas.DataFrame(my_dict)
for (k, v) in my_data_frame.items():
    print(k)
    print(v)

# loop through rows of a data frame
for (index, row) in my_data_frame.iterrows():
    if row.Name == "Ali":
        print(row.Score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("./data/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
get_user_word = True

while get_user_word:
    user_word = input("Enter your word: ").upper()
    try:
        user_nato_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabets please")
    else:
        print(user_nato_list)
        get_user_word = False

