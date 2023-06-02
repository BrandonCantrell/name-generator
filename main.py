import json
import random


def read_list(filename):
    a = open(filename, "r")
    adj_data = a.read()
    return adj_data.split("\n")

if __name__ == "__main__":
    food_name = random.choice(read_list('foods.list'))
    adj_str = random.choice(read_list('adjectives.list'))
    print("Release name: " + adj_str.title() + ' ' + food_name)
