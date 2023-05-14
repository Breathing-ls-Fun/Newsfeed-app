from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from newsfeed.reporter.reporter import Reporter
from newsfeed.reporter.weatherman import Weatherman

def home(request):
    news_api_key = 'd1232f6fd9ad400da947bf5a59963e10'
    weather_api_key = '33acb338cf186037e1f0801d8945e21b'

    reporter = Reporter(news_api_key)
    weather = Weatherman(weather_api_key, location = 'New York')

    topnews = reporter.get_top_headlines()
    forecast = weather.get_current_weather()

    print (topnews)
    print (forecast)

    hi = round(forecast['hi'])
    lo = round(forecast['lo'])
    current_temp = round(forecast['temp'])
    status = forecast['status']
    icon = forecast['icon_url']

    weather_data = {
        "hi": hi,
        "lo": lo,
        "current": current_temp,
        "status": status,
        "icon": icon
    }

    latest = topnews['articles']
    title = []
    desc = []
    url = []
    author = []
    date = []
    image = []

    for i in range(len(latest)):
        news = latest[i]

        title.append(news['title'])
        desc.append(news['description'])
        url.append(news['url'])
        author.append(news['author'])
        date.append(news['publishedAt'])
        image.append(news['urlToImage'])

    all_news = zip(title, desc, url, author, date, image)

    context = {
        'weather_data': weather_data,
        'all_news': all_news,
    }
    
    return render(request, 'home.html', context)

 

    




