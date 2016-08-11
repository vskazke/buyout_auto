# -*- coding: utf-8 -*-

import requests
# from urllib import quote
from slugify import Slugify, CYRILLIC
from models import Models


def brand_auto():
    list_brands = []
    page = requests.get('http://catalog.am.ru/').text
    all_brands = page.split\
            ('<div class="au-grids au-openable-list-body">')[1].split\
            ('<div class="au-openable-panel js-openable-list__sh">')[0]
    all_brands = all_brands.split('<a')
    for brand in all_brands[1:]:
        brands = {}
        if brand.find('title') > 0:
            brands['url'] = brand.split('href="')[1].split('"')[0]
            brands['title'] = brand.split('title="')[1].split('"')[0]
            if brands['title'] != 'Ferrari' and brands['title'] != 'TVR':
                list_brands.append(brands)
    return list_brands


def model_auto():
    all_auto = []
    all_brands = brand_auto()
    for brand in all_brands:
        auto = {}
        models= []
        page = requests.get(brand['url']).text
        title = page.split('<title>')[1].split('</title>')[0]
        print(title)
        all_models = page.split('<div class="au-grids au-openable-list-body">')[1]
        all_models = all_models.split('title="')
        for one in all_models[1:]:
            title = one.split('"')[0]
            models.append(title)
        auto['brand'] = brand['title']
        auto['models'] = models
        all_auto.append(auto)
        Models.create(
            brand=auto['brand'],
            models=auto['models'])
    return all_auto


def main():
    #  brand_auto()
    for auto in Models.select().where(Models.brand == 'УАЗ'):
        print( auto)


if __name__ == '__main__':
    main()

