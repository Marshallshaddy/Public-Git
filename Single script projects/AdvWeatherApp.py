import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

def get_weather_data(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9229757a39bd973a1efb207a3443a65e&units=metric"
        response = requests.get(url)
        data = response.json()
        if "message" in data:
            print(f"Error retrieving data from OpenWeatherMap: {data['message']}")
            return None
        return data
    except Exception as e:
        print(f"An error occurred while retrieving the weather data: {e}")
        return None

def display_weather_data():
    global city_entry
    city = city_entry.get()
    weather_data = get_weather_data(city)
    if weather_data is not None:
        weather_window = tk.Toplevel()
        weather_window.title("Weather Data")
        weather_frame = ttk.Frame(weather_window)
        temperature_label = ttk.Label(weather_frame, text="Temperature:")
        humidity_label = ttk.Label(weather_frame, text="Humidity:")
        wind_label = ttk.Label(weather_frame, text="Wind:")
        temperature_text = ttk.Label(weather_frame, text=weather_data['main']['temp'])
        humidity_text = ttk.Label(weather_frame, text=weather_data['main']['humidity'])
        wind_text = ttk.Label(weather_frame, text=weather_data['wind']['speed'])
        temperature_label.grid(row=0, column=0)
        temperature_text.grid(row=0, column=1)
        humidity_label.grid(row=1, column=0)
        humidity_text.grid(row=1, column=1)
        wind_label.grid(row=2, column=0)
        wind_text.grid(row=2, column=1)
        weather_frame.pack()
        weather_window.mainloop()
    else:
        messagebox.showerror("Error", "Invalid city name or other error occurred.")

def main():
    root = tk.Tk()
    root.title("Weather App")
    global city_entry
    city_label = tk.Label(root, text="Enter city name")
    city_entry = tk.Entry(root)
    get_weather_button = tk.Button(root, text="Get Weather", command=display_weather_data)
    city_label.pack()
    city_entry.pack()
    get_weather_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
