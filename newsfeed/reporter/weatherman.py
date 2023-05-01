from pyowm import OWM

class Weatherman:
    current_weather = {}
    daily_forecast = []

    def __init__(self, key=None, location=None, tmp_units='fahrenheit'):
        self.owm = OWM(key)
        self.location = location
        self.weather_manager = self.owm.weather_manager()
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
        prev = self.location
        self.location = location
        try:
            self.weather_manager.weather_at_place(self.location)
        except:
            self.location = prev

    def get_daily_forecast(self, img_size='2x'):
        try:
            observation = self.weather_manager.forecast_at_place(self.location,'3h').forecast
            observation.actualize()
        except:
            return self.daily_forecast
        self.daily_forecast.clear()
        day_index = observation.get(0).reference_time('date').date()
        tmp_hi = -1
        tmp_lo = 9999
        tmp_avg = 0
        status_count = {}
        status_icon = {}
        i = 1
        for day in observation:
            new_day_index = day.reference_time('date').date()
            temperature = day.temperature(self.tmp_units)

            if new_day_index != day_index:
                tmp = {}
                tmp['date'] = day_index
                tmp['hi'] = tmp_hi
                tmp['lo'] = tmp_lo
                tmp['temp'] = round(tmp_avg/i, 2)
                tmp['status'] = max(status_count, key=status_count.get)
                tmp['icon_url'] = status_icon[tmp['status']]
                self.daily_forecast.append(tmp)
                i = 1
                tmp_hi = -1
                tmp_lo = 9999
                tmp_avg = 0
                status_count = {}
                day_index = new_day_index
            
            tmp_hi = max(temperature['temp_max'],tmp_hi)
            tmp_lo = min(temperature['temp_min'],tmp_lo)
            tmp_avg += temperature['temp']
            if day.detailed_status in status_count:
                status_count[day.detailed_status] += 1
            else:
                status_count[day.detailed_status] = 1
            status_icon[day.detailed_status] = day.weather_icon_url(img_size)
            i+= 1

        return len(self.daily_forecast), self.daily_forecast


