import tkinter as tk
import requests

# OpenWeatherMap API Key
API_KEY = "6df154cdff3f2489b61ad99833d7ed70"  # Apna API key yahan daalain
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data from the API
def get_weather(city):
    complete_url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    print("Requesting URL:", complete_url)  # Debug
    response = requests.get(complete_url)
    data = response.json()
    print("API Response:", data)  # Debug

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]

        return f"Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}"
    else:
        return f"City not found!\n{data.get('message', '')}"


# Function to display weather in the UI
def show_weather():
    city = city_name_entry.get()
    weather_info = get_weather(city)
    weather_label.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create the user interface
city_name_label = tk.Label(root, text="Enter City Name:")
city_name_label.pack()

city_name_entry = tk.Entry(root)
city_name_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

# Run the application
root.mainloop()
