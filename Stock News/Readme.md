## Stock News


STEP 1: Use https://www.alphavantage.co/documentation/#daily

1(a) : When stock price increase/decreases by 5%(or any threshold) between yesterday and the day before yesterday.


```
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
```

1(b): Find the positive difference between 1 and 2. e.g. 20 - 40 = -20, 
```
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
```

1(c) : Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

STEP 2: https://newsapi.org/
If percentage is greater than 5 then print("Get News").
Get the first 3 news pieces for the COMPANY_NAME.



STEP 3: Use twilio.com/docs/sms/quickstart/python to send a separate message with each article's title and description to your phone number.
Create a new list of the first 3 article's headline and description using list comprehension.
Send each article as a separate message via Twilio.

Dependencies Tools/Libraries
Python 3+
JSON
Twilio
Requests
