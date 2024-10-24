import psycopg2
import json
from project_tp import settings

def find_dishes(products: [str]):# -> str:
    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    cursor = connection.cursor()
    cursor.execute(f"""
SELECT ingredients.dish_id FROM ingredients
JOIN products ON products.product_id = ingredients.product_id
WHERE products.name IN ({str(products)[1:-1]});""")
    ids = cursor.fetchall()
    new_ids = str(ids)[2:-3].split(',), (')
    appropriate_dish_ids = find_3_most_matching(new_ids)
    result = []
    for id in appropriate_dish_ids:
        if id == '':
            break
        cursor.execute(f"""
SELECT dishes.dish_name, dishes.recepy, dishes.time FROM dishes 
WHERE dishes.dish_id = {id};""")
        record = cursor.fetchall()
        result += [{'name': record[0][0], 'recipy': record[0][1], 'time': str(record[0][2])}]

    cursor.close()
    connection.close()

    return json.dumps(result, ensure_ascii=False).encode('utf8').decode()


def find_3_most_matching(ids: []):
    dishes = dict()
    for id in ids:
        dishes[id] = 1 if (id not in dishes.keys()) else dishes[id] + 1
    max_3 = [-1, -1, -1]
    max_3_id = ['', '', '']
    for id in dishes.keys():
        if dishes[id] > max_3[0]:
            max_3_id[0] = id
            max_3[0] = dishes[id]
        elif dishes[id] > max_3[1]:
            max_3_id[1] = id
            max_3[1] = dishes[id]
        elif dishes[id] > max_3[2]:
            max_3_id[2] = id
            max_3[2] = dishes[id]
    return max_3_id

