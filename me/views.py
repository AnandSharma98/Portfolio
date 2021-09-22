from django.shortcuts import render
from .models import Home, About, Category, Designs


def home(request):
    # Home
    home = Home.objects.latest('updated')  # to get latest data

    # About
    about = About.objects.latest('updated')

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Designs.objects.all()

    context = {
        'home': home,
        'about': about,
        'categories': categories,
        'designs': portfolios
    }

    return render(request, 'me/index.html', context)
