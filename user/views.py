import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from newsfeed.reporter.reporter import Reporter


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect('/user/personal_home')
            return redirect('home')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,username=username)
                user.set_password(password)
                user.save()
                print("Account created!")
                return redirect('/user/login')
        
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, "user/registration.html")


def query(request):
    api_key = 'd1232f6fd9ad400da947bf5a59963e10'
    reporter = Reporter(api_key)
    
    query = request.GET['query']
    topnews = reporter.search_articles(query)

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
        'all_news': all_news,
        'query': query
    }

    return render(request,'user/query.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def preferences(request):
    user_categories = ['Sports', 'Tech', 'Art', 'Business', 'Health']  # Example list of categories

    if request.method == 'POST':
        # Handle form submission and store preferences
        location = request.POST.get('location')
        category1 = request.POST.get('category1')
        category2 = request.POST.get('category2')
        category3 = request.POST.get('category3')

        # Store the preferences in the user's session
        request.session['location'] = location
        request.session['category1'] = category1
        request.session['category2'] = category2
        request.session['category3'] = category3

        return redirect('home')  # Redirect to the desired page after storing preferences
    else:
        context = {
            'user_categories': user_categories
        }
        return render(request, 'user/preferences.html', context)