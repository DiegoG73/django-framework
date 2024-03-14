from django.shortcuts import render, HttpResponse


# Create your views here.
html_base="""
    <h1>My personal web</h1>
    <ul>
        <li> <a href="/">Portrait</a> </li>
        <li> <a href="/about-me/">About</a> </li>
        <li> <a href="/portfolio/">Portfolio</a> </li>
        <li> <a href="/contact-me/">Contact</a> </li>
    </ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")
    
def portfolio(request):
    return render(request, "core/portfolio.html")
    
def contact(request):
    return render(request, "core/contact.html")