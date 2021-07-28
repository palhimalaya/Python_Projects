import smtplib
import datetime as dt
import random

my_email = "4testingcode@gmail.com"
password = "testingcode4@()"

# .................................Get current day.........................#
now = dt.datetime.now()
day_of_week = now.weekday()

# print(day_of_week)
# date_of_birth = dt.datetime(year=2000, month=9,day=24)
# print(date_of_birth)
# .................................Check current day with provided day and send mail.........................#
if day_of_week == 4:
    # .................................Read file.........................#
    with open("quotes.txt") as file:
        quotes = file.readlines()
        # quotes = [line for line in file]
        random_quotes = random.choice(quotes)
        print(random_quotes)
    # .................................Send Quotes.........................#
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="palhimalaya123@gmail.com",
                            msg=f"Subject:Quotes\n\n{random_quotes}")

