import smtplib
import datetime as dt
import pandas
from random import choice, randint

my_email = "XX@gmail.com"


# An App Password must be added for gmail account and copy it here
password = "XXXX"

host_dic = {
    'Gmail': 'smtp.gmail.com',
    'Hotmail': 'smtp.live.com',
    'Outlook': 'outlook.office365.com',
    'Yahoo': 'smtp.mail.yahoo.com',
}


def send_email_to(host, email, subject, message):
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:{subject}\n\n{message}")


def create_birthdays_dict(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pandas.read_csv(csv_file)

    # Create an empty dictionary to store the birthday data
    birthdays_dict = {}

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Extract the month, day, and other data from the current row
        birthday_month = row['month']
        birthday_day = row['day']
        data_row = (row['name_'], row['email'], row['year'])

        # Create a tuple key for the dictionary
        birthday_key = (birthday_month, birthday_day)

        # Add the data row to the dictionary, creating a list if the key already exists
        birthdays_dict.setdefault(birthday_key, []).append(data_row)

    return birthdays_dict


def send_birthday_wish():
    today = (dt.datetime.now().month, dt.datetime.now().day)

    data_frame = pandas.read_csv("birthdays.csv")

    send_email_to_list = []

    month_day_dict = {(row.month, row.day): (row.name_, row.email) for (index, row) in data_frame.iterrows()}
    for k, v in month_day_dict.items():
        if k == today:
            send_email_to_list.append(v)

    for person in send_email_to_list:
        letter_index = randint(1, 3)
        letter_path = f"./letter_templates/letter_{letter_index}.txt"

        with open(letter_path) as f:
            content = f.read()

        content = content.replace("[NAME]", person[0])
        send_email_to(host=host_dic["Gmail"], email=person[1], subject="Happy Birthday", message=content)


def send_birthday_wish2():
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)

    data = pandas.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name_"])

        send_email_to(host=host_dic["Gmail"], email=birthday_person["email"],
                      subject="Happy Birthday", message=contents)


def send_today_quote(day):
    weekday = dt.datetime.now().weekday()

    if weekday == day:
        with open("quotes.txt") as f:
            quote_list = f.readlines()
            send_email_to(host=host_dic["Yahoo"], email="mansy_gh@yahoo.com", subject="Hello",
                          message=choice(quote_list))


send_birthday_wish2()
# birthdays_dict = create_birthdays_dict("birthdays.csv")
