import smtplib
import datetime as dt

MAIL_HOST = ""
MAIL_PORT = 0
MAIL_USERNAME = ""
MAIL_PASSWORD = ""
MAIL_NOREPLY = ""

with smtplib.SMTP(MAIL_HOST, MAIL_PORT) as connection:
    connection.starttls()
    connection.login(MAIL_USERNAME, MAIL_PASSWORD)
    connection.sendmail(MAIL_NOREPLY, "econceicao@technoplus.co.mz", "Hello SMTP World")
    # connection.close()

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
week_day = now.weekday()

random_day = dt.datetime(year=2022, month=4, day=14)

print(now)
print(year)
print(month)
print(day)
print(week_day)
print(random_day)