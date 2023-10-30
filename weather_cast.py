"""Module generating weather information. """
import subprocess
import argparse
def install_library(library_name):
    """This is to install a library"""
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"Successfully installed {library_name}.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library_name}.")
try:
    import requests
except ModuleNotFoundError:
    install_library("requests")
    import requests


def get_weather(city):
    "generates weather information from api"
    api_key = "a5ebcfe9d324fee906dbb6e1902dbfbb"
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}",timeout=59)
    return weather_data.json()

def weather_dir(weather_data):
    "makes directory with weather information"
    md = {}
    md['temperature'] = weather_data["main"]["temp"]
    md['weather_description'] = weather_data['weather'][0]["description"]
    md['pressure'] = weather_data['main']['pressure']
    md['humidity'] = weather_data['main']['humidity']
    md['wind_speed'] = weather_data['wind']['speed']
    return md

def main():
    "main part where everything is called"
    parser = argparse.ArgumentParser(description='Information conserning weather: ')
    parser.add_argument('city_name', type=str, help='Enter a city name: ', nargs="+")
    parser.add_argument('--par', type=str, help='Enter a+the weather  parametrs that you need: ', nargs="+")
    args = parser.parse_args()
    weather_data = get_weather(args.city_name)
    if weather_data['cod'] == '404':
        print("City not found")
        return None    
    my_weather = weather_dir(weather_data)
    if args.par:
        for el in args.par:
            print(my_weather[el])
    else:
        print(my_weather)
    return None
    

main()
