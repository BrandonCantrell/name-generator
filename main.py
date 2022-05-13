import json
import random


def food_data():
    f = open('food.json', "r")
    food_data = json.loads(f.read())

    return food_data

def adjectives():
    a = open('adjectives.list', "r")
    adj_data = a.read()
    adj_list = adj_data.split(",")

    return adj_list

def restaurants():
    res_list = []
    for res in food_data():
        res_list.append(res['restaurant'])

    if not None:
        return res_list

def food_names():
    food_name_list = []
    for i in food_data():
        for x in (i['foodItems']):
            food_name_list.append((x['foodName']))

    return food_name_list

if __name__ == "__main__":


    food_name = random.choice(food_names())

    adj_str = random.choice(adjectives())

    print("Release name:" + adj_str.title() + ' ' + food_name)



