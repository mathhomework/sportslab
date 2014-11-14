import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from scrapyd_api import ScrapydAPI

from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt
from pymongo import Connection

con = Connection(
    host=getattr(settings, "MONGODB_HOST", None),
    port=getattr(settings, "MONGODB_PORT", None)
)[settings.MONGODB_DATABASE]

if getattr(settings, "MONGODB_USERNAME", None):
    con.authenticate(getattr(settings, "MONGODB_USERNAME", None), getattr(settings, "MONGODB_PASSWORD", None))

# db = con.training
# sportslab = db.sportslab

def search(request):

    return render(request, "search.html")
#     db.users.

@csrf_exempt
def do_scrape(request):
    print "do scrape!!"
    if request.method == "POST":
        data = json.loads(request.body)
        url = "http://localhost:6800/schedule.json"
        # test = "http://www.maxpreps.com/high-schools/jserra-catholic-lions-(san-juan-capistrano,ca)/football/stats.htm"
        payload = {
            "project": "sportslab_scrape_outer",
            "spider": "max",
            "max_url": data["link"]
        }
        r = requests.post(url, data=payload)
        print data['link']
    return HttpResponse("Yo")

