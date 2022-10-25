import requests

api_key = input("add you API key:\n")

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    return requests.get(url).json()

def get_weather_for_city(city):
    response = get_city_coordinates(city)[0]
    city = response.get("name")
    state = response.get("state")
    country = response.get("country")
    lat = response.get("lat")
    lon = response.get("lon")
    request = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(request).json()
    print(f"Showing weather for {city}, {state}, {country}:")
    print(response.get("weather")[0].get("description"))
    print("Temperature: ", response.get("main").get("temp"), "°C", sep="")
    print("Temperature Max: ", response.get("main").get("temp_max"), "°C", sep="")
    print("Temperature Min: ", response.get("main").get("temp_min"), "°C", sep="")

get_weather_for_city(input("Search weather for city?\n"))