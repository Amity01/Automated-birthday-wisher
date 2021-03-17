# # ##################### Extra Hard Starting Project ######################
# import datetime as dt
# import smtplib
# import random
#
# import pandas
#
# my_email = "amityad572001@gmail.com"
# password = "harm253125"
#
#
# def send_letter(i):
#     global name_list, email_list
#     random_num = random.randint(1, 3)
#     with open(f"letter_templates/letter_{random_num}.txt") as letter:
#         letter_line = letter.read()
#         letter_line = letter_line.replace("NAME", name_list[i])
#     print(letter_line)
#     with open(smtplib.SMTP("smtp.gmail.com")) as connection:
#         connection.starttls()
#         connection.login(email=my_email, password=password)
#         connection.sendmail(my_email, email_list[i], f"Subject:Happy Birthday\n\n{letter_line}")
#
#
# today = dt.datetime.now()
# today_month = today.month
# today_day = today.day
#
# data = pandas.read_csv("birthdays.csv")
# month_list = data["month"].to_list()
# day_list = data["day"].to_list()
# email_list = data["email"].to_list()
# name_list = data["name"].to_list()
# for i in range(len(month_list)):
#     if month_list[i] == today_month and day_list[i] == today_day:
#         send_letter(i)

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "Your email"
MY_PASSWORD = "your password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")