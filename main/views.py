from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.core import serializers
import psycopg2
import json
from project_tp import settings


def index(request):
    return render(request, "main/index.html")


def get_recipy(request: HttpRequest):
    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    # TODO: parse json in request. Variables below are just for testing.
    food = ['Картошка', 'Чеснок']
    amount = [3, 2]

    cursor = connection.cursor()
    cursor.execute(f"""
WITH products_with_amount AS (
    SELECT unnest(ARRAY{food.__str__()}) AS product_name,
           unnest(ARRAY{amount.__str__()}) AS max_amount
)
SELECT dishes.dish_name, dishes.recepy, dishes.time, dishes.dish_quisine FROM ingredients 
JOIN dishes ON ingredients.dish_id = dishes.dish_id 
JOIN products ON products.product_id = ingredients.product_id
JOIN products_with_amount pwa ON products.name = pwa.product_name
WHERE ingredients.amount <= pwa.max_amount;
    """)
    intermediate_obj = cursor.fetchall()

    cursor.close()
    connection.close()

    result = []
    for record in intermediate_obj:
        result += [{'name': record[0], 'recipy': record[1], 'time': str(record[2]), 'cuisine': record[3]}]

    return HttpResponse(json.dumps(result, ensure_ascii=False).encode('utf8').decode())
