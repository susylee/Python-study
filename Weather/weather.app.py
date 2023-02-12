import tkinter as tk
from tkinter import messagebox
from tkinter import font
from configparser import ConfigParser
import requests


url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #(City, Country, temp_celcius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin -273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)    
        return final

    if result:
        print(result.content)
    else:
        return None

# print(get_weather('London'))



def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather :
        location_lbl['text'] = '{}. {}.format(weather[0], weather[1])'
        image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F.format(weather[2], weather[3])'
        weather_lbl['text'] = weather[5]

    else:
        messagebox.showerror('Error', 'Cannot find city {}.format(city)')



app=tk.Tk()
app.title("weather app")
app.geometry("700x350")

city_text = tk.StringVar()
city_entry = tk.Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = tk.Button(app, text='Search weather', width = 12, command=search)
search_btn.pack()

location_lbl = tk.Label(app, text='', font=('bold', 20))
location_lbl.pack()

image = tk.Label(app, bitmap='')
image.pack()

temp_lbl = tk.Label(app, text='')
temp_lbl.pack()

weather_lbl = tk.Label(app, text='')
weather_lbl.pack()


app.mainloop()