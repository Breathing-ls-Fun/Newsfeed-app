from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from newsapi import NewsApiClient
from newsfeed.reporter.reporter import Reporter

def home(request):
    api_key = 'fcdda744f1d94e9199337e419a17be4a'
    reporter = Reporter(api_key)
    topnews = reporter.get_top_headlines()

    print (topnews)
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
        'all_news': all_news
    }
    
    return render(request, 'home.html', context)

def category(request, category):
    api_key = 'fcdda744f1d94e9199337e419a17be4a'
    reporter = Reporter(api_key)
    topnews = reporter.get_top_headlines(category)

    print (topnews)
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
        'all_news': all_news
    }
    
    return render(request, 'category.html', context)
 

    




