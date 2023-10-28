import json
import tkinter as tk
from tkinter import ttk

def get_weather_data(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=API_KEY&units=metric&humidity&wind&uvi"
    response = requests.get(url)
    data = response.json()
    return data

def save_weather_data(city):
    weather_data = get_weather_data(city)
    with open('weather_data.json', 'w') as f:
        json.dump(weather_data, f)

def display_weather_data():
    city = city_entry.get()
    weather_data = get_weather_data(city)

    # Create a new window to display the weather data
    weather_window = tk.Toplevel()
    weather_window.title("Weather Data")

    # Create a frame to hold the weather data
    weather_frame = ttk.Frame(weather_window)

    # Create a label for each piece of weather data
    temperature_label = ttk.Label(weather_frame, text="Temperature:")
    humidity_label = ttk.Label(weather_frame, text="Humidity:")
    wind_label = ttk.Label(weather_frame, text="Wind:")
    uvi_label = ttk.Label(weather_frame, text="UV Index:")

    # Create a text box for each piece of weather data
    temperature_text = ttk.Entry(weather_frame, width=10)
    humidity_text = ttk.Entry(weather_frame, width=10)
    wind_text = ttk.Entry(weather_frame, width=10)
    uvi_text = ttk.Entry(weather_frame, width=10)

    # Place the labels and text boxes on the frame
    temperature_label.grid(row=0, column=0)
    temperature_text.grid(row=0, column=1)
    humidity_label.grid(row=1, column=0)
    humidity_text.grid(row=1, column=1)
    wind_label.grid(row=2, column=0)
    wind_text.grid(row=2, column=1)
    uvi_label.grid(row=3, column=0)
    uvi_text.grid(row=3, column=1)

    # Pack the frame into the window
    weather_frame.pack()

    # Display the window
    weather_window.mainloop()


def main():
    root = tk.Tk()
    root.title("Weather App")

    # Create a label for the city entry
    city_label = tk.Label(root, text="Enter city name:")

    # Create an entry for the city name
    city_entry = tk.Entry(root)

    # Create a button to get the weather data
    get_weather_button = tk.Button(root, text="Get Weather", command=display_weather_data)

    # Place the label, entry, and button on the root window
    city_label.pack()
    city_entry.pack()
    get_weather_button.pack()

    # Start the mainloop
    root.mainloop()


if __name__ == "__main__":
    main()
