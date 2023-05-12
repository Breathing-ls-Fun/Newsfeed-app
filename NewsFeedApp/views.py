from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from newsapi import NewsApiClient

def home(request):
    newsapi = NewsApiClient(api_key='fcdda744f1d94e9199337e419a17be4a')
    topnews = newsapi.get_top_headlines(language='en')
    latest = topnews['articles']
    title = []
    desc = []
    url = []
    author = []
    date = []

    for i in range(len(latest)):
        news = latest[i]

        title.append(news['title'])
        desc.append(news['description'])
        url.append(news['url'])
        author.append(news['author'])
        date.append(news['publishedAt'])

    all_news = zip(title, desc, url, author, date)

    context = {
        'all_news': all_news
    }
    
    return render(request, 'home.html', context)

 

    




