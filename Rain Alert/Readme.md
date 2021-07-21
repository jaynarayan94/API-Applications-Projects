<h2>Rain Alert</h2>

Make one API call using Weather API to extract the Hourly forecast for the next 11 hrs of the day then extract the current.weather.id(Weather condition id) for those 11 hrs and If the id is less than 700 that means it may rain that day.
If the id value is less then 700 using [Twillio](https://www.twilio.com/) a message is triggered to my personal phone. Giving a reminder message to carry a umberella that day.


Scheduled to run this script daily at 9:00 AM IST time using [pythonanywhere's cloud](https://www.pythonanywhere.com/)


API call (end point with the parameters):

https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

```
parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": weather_api_key,
        "exclude": "current,minutely,daily,alerts"
    }
```

[Weather codintion id Reference](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)


<span>
<img src="https://github.com/jaynarayan94/API-Applications-Projects/blob/main/Rain%20Alert/Rain%20%26%20Stock%20Alert.jpeg" width=500px height="450px" />
</span>
