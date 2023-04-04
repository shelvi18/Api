from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=science')
    posts = response.json()
    posts
    return render(request,'index.html',{'data':data})


