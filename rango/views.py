from django.http import HttpResponse

def index(Request):
    return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about_page(Request):
    return HttpResponse("Rango Says: Here is the about page. <a href='/rango'>Index</a>")
