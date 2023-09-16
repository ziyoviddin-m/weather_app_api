from django.http import HttpResponseRedirect
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = 'ce6d495665011b838b985a58995df78f'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()[::-1]
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if "main" in res:
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                'id': city.id
            }
            all_cities.append(city_info)

    context = {'all_cities': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def delete(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
