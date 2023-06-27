from django.shortcuts import render
from dish_search_application.models import Dish

def search(request):
    query = request.GET.get('query')
    if query:
        dishes = Dish.objects.filter(name__icontains=query)
    else:
        dishes = Dish.objects.all()
    return render(request, 'search.html', {'dishes': dishes, 'query': query})
