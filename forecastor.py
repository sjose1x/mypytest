
import random

class WeatherService:
    def barometer(self):
        return random.choise(['rising','falling'])#Non deterministic

class ForeCaster:
    def __init__(self, weatherservice):
        self.weatherservice = weatherservice
    
    def forecast(self):
        reading = self.weatherservice.barometer()
        forcast_dict = dict(
        rising ='Going to Rain',
        falling = 'Looks Clear'
        )
        return forcast_dict[reading]