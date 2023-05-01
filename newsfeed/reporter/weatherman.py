from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

class Weatherman:
    current_weather = {}
    daily_forecast = None

    def __init__(self, key=None, location=None, tmp_units='fahrenheit'):
        self.weather_manager = OWM(key).weather_manager()
        self.location = location
        self.tmp_units = tmp_units

    def get_current_weather(self, img_size="2x"):
        try:
            observation = self.weather_manager.weather_at_place(self.location)
        except:
            return self.current_weather
        report = observation.weather
        temperature = report.temperature(self.tmp_units)
        self.current_weather['hi'] = temperature['temp_max']
        self.current_weather['lo'] = temperature['temp_min']
        self.current_weather['temp'] = temperature['temp']
        self.current_weather['status'] = report.detailed_status
        self.current_weather['icon_url'] = report.weather_icon_url(img_size)
        return self.current_weather
    
    def update_location(self, location):
        self.location = location

