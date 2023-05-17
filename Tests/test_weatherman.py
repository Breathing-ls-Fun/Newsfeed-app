from newsfeed.reporter.weatherman import Weatherman
import pytest
import time

@pytest.fixture(scope="session", autouse=True)
def weatherman():
    print("\nTesting API Connection\n")
    start_time = time.process_time()
    weatherman = Weatherman(key='33acb338cf186037e1f0801d8945e21b',location='New York, New York')
    print(time.process_time() - start_time, "seconds")
    return weatherman

def test_get_current_weather(weatherman):
    print("\nTesting Get Current Weather\n")
    start_time = time.process_time()
    test_weather = weatherman.get_current_weather()
    print(test_weather)
    print(time.process_time() - start_time, "seconds")
    assert(type(test_weather['hi']) == float and type(test_weather['lo']) == float and type(test_weather['temp']) == float)
    assert(test_weather['hi'] >= test_weather['lo'] and test_weather['temp'] >= test_weather['temp'] and test_weather['hi'] >= test_weather['temp'])
    assert(type(test_weather['status']) == str and type(test_weather['icon_url']) == str)

def test_update_location(weatherman):
    print("\nTesting Update Location\n")
    test_location = 'Berlin,Germany'
    start_time = time.process_time()
    test_weather = weatherman.update_location(test_location)
    print(test_weather)
    print(time.process_time() - start_time, "seconds")
    assert(weatherman.location == test_location)

def test_invalid_location(weatherman):
    print("\nTesting Invalid Location\n")
    test_location = 'jjdsjdksdaasd,Germany'
    start_time = time.process_time()
    prev = weatherman.get_current_weather()
    prev_location = weatherman.location
    test_weather = weatherman.update_location(test_location)
    test_weather = weatherman.get_current_weather()
    print(test_weather)
    print(time.process_time() - start_time, "seconds")    
    assert(weatherman.location == prev_location)
    assert(test_weather == prev)

def test_daily_forecast(weatherman):
    print("\nTesting Daily Forecast\n")
    start_time = time.process_time()
    test_weather_forecast = weatherman.get_daily_forecast()
    print(test_weather_forecast)
    print(time.process_time() - start_time, "seconds")
    assert(test_weather_forecast[0] == 5 == len(test_weather_forecast[1]))
    for test_weather in test_weather_forecast[1]:
        assert(type(test_weather['hi']) == float and type(test_weather['lo']) == float and type(test_weather['temp']) == float)
        assert(test_weather['hi'] >= test_weather['lo'] and test_weather['temp'] >= test_weather['temp'] and test_weather['hi'] >= test_weather['temp'])
        assert(type(test_weather['status']) == str and type(test_weather['icon_url']) == str)