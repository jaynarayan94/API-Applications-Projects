import smtplib
import datetime as dt
import random

my_email = "jaynd194@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password = "Jaynarayan@20")
        connection.sendmail(from_addr= my_email,
                            to_addrs = "jaynarayan94@gmail.com",
                            msg = f"Subject:Daily Motivations\n\n {quote}")


