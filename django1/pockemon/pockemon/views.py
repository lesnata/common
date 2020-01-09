from django.http import HttpResponse
import requests
import json
from django.shortcuts import render


def health_check(request):
    return HttpResponse("Health is OK")


def index(request):
    return render(request, 'index.html')


def good_reads(request):
    # test with ISBN: 1632168146
    goodreads_key = 'OSSf0NDlODo3VveMME01w'

    reviews = requests.get("https://www.goodreads.com/book/review_counts.json",
                          params={"key": goodreads_key, "isbns": 1632168146})
    good_reads_data = reviews.json()

    return render(request, 'good-reads.html', {
        "reviews": good_reads_data["books"][0]["reviews_count"],
        "average_rating": good_reads_data["books"][0]["average_rating"]
    })

    # return render(request, 'good-reads.html', {
    #     "title": good_reads_data['title'],
    #     "author": good_reads_data['author'],
    #     "year": good_reads_data['year'],
    #     "isbn": good_reads_data['isbn']
    # })

    # if result.status_code != 200:
    #     return HttpResponse("Error")
    # return result.json()












# POCKEMON_URL = 'https://pokeapi.co/api/v2/'
# def get_pockemon():
#     response = requests.get(f'{POCKEMON_URL}/type/3')
#     return response.json()
#
# def pokemons(request):
#     latest_pokemon_list = [f"{p['pokemon']['name']}" for p in get_pockemon()['pokemon']]
#     context = {'latest_pokemon_list': latest_pokemon_list}
#     return render(request, 'pokemons.html', context)


# def mypage(request):
#     pokemons = requests.get(POKEMON_API + 'type/3').json()['pokemon']
#     raw_response = [f"<li>{item['pokemon']['name']}</li>" for item in pokemons]
#     pokemon_html_list = "<a href='/'>Back to the homepage</a>\n<ol>\n"
#     for p in raw_response:
#         pokemon_html_list += p
#     response = pokemon_html_list + "\n</ol>"
#     return HttpResponse(response)


