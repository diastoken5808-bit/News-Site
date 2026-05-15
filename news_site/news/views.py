from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from .models import SearchQuery
from django.contrib import messages


NEWS_API_KEY = "2189ac98fb6844188191cb5cbf42acee"

def news_list(request):
    query = request.GET.get('q', 'Tesla')

    try:
        num = int(request.GET.get('num', 5))
    except:
        num = 5

    if num > 20:
        num = 20
    if num < 1:
        num = 1

    if request.user.is_authenticated:
        SearchQuery.objects.create(
            user=request.user,
            query=query,
            num=num
        )

    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=20&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    raw_articles = data.get('articles', [])

    cleaned = [
        a for a in raw_articles
        if a.get('title') and a.get('description')
    ]

    articles = cleaned[:num]

    return render(request, 'news/news_List.html', {
        'articles': articles,
        'query': query,
        'num': num
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('/login/')

        if password1 != password2:
            messages.error(request, "Пароли не совпадают")

    return render(request, 'registration/register.html')

