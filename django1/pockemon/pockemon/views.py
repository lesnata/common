from django.http import HttpResponse
import requests
from django.shortcuts import render


def health_check(request):
    return HttpResponse("Health is OK")


def index(request):
    return render(request, 'index.html')


def good_reads(request):
    # testing with ISBN: 1632168146
    goodreads_key = 'OSSf0NDlODo3VveMME01w'
    reviews = requests.get("https://www.goodreads.com/book/review_counts.json",
                           params={"key": goodreads_key, "isbns": 1632168146})
    good_reads_data = reviews.json()
    return render(request, 'good-reads.html', {
        "reviews": good_reads_data["books"][0]["reviews_count"],
        "average_rating": good_reads_data["books"][0]["average_rating"]
    })
