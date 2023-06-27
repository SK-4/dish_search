import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dish_search.settings')
django.setup()

from django.db import transaction
from dish_search_application.models import Dish

@transaction.atomic
def import_dishes_from_csv():
    with open('C:/Users/soham/Desktop/one_last_dance/dish_search/dish_search/restaurants_small.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dish_name = row[1]  # Assuming the dish name is in the second column
            Dish.objects.create(name=dish_name)

if __name__ == '__main__':
    import_dishes_from_csv()
