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
    current = weather.get_current_weather()
    weekly_forecast = weather.get_daily_forecast()

    print (current)
    print (weekly_forecast)

    hi = round(current['hi'])
    lo = round(current['lo'])
    current_temp = round(current['temp'])
    status = current['status']
    icon = current['icon_url']

    current_data = {
        "hi": hi,
        "lo": lo,
        "current": current_temp,
        "status": status,
        "icon": icon
    }

    weekly_date = []
    weekly_hi = []
    weekly_lo = []
    weekly_status = []
    weekly_icon = []

    for data in weekly_forecast:
        weekly_date.append(str(data['date']))
        weekly_hi.append(round(data['hi']))
        weekly_lo.append(round(data['lo']))
        weekly_status.append(data['status'])
        weekly_icon.append(data['icon_url'])

    weekly_data = zip(weekly_date, weekly_hi, weekly_lo, weekly_status, weekly_icon)

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
        'current_data': current_data,
        'weekly_data': weekly_data,
        'all_news': all_news,
    }
    
    return render(request, 'home.html', context)

 

    




