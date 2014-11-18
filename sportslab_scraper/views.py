import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt
from pymongo import Connection, ASCENDING

# db = Connection(
#     host=getattr(settings, "MONGODB_HOST", None),
#     port=getattr(settings, "MONGODB_PORT", None)
# )[settings.MONGODB_DATABASE]
# #
# if getattr(settings, "MONGODB_USERNAME", None):
#     db.authenticate(getattr(settings, "MONGODB_USERNAME", None), getattr(settings, "MONGODB_PASSWORD", None))

# # db = con.training
# # sportslab = db.sportslab
connection = Connection('mongodb://andrew:hotdog@ds053190.mongolab.com:53190/sportslab_mongodb')
db = connection['sportslab_mongodb']
collection = db['sportslab']

def search(request):
    return render(request, "search.html")


@csrf_exempt
def do_scrape(request):
    print "do scrape!!"
    if request.method == "POST":
        data = json.loads(request.body)
        # running locally
        # url = "http://localhost:6800/schedule.json"
        # aws
        url = "http://ec2-54-67-31-196.us-west-1.compute.amazonaws.com:6800/schedule.json"
        payload = {
            "project": "sportslab_scrape",
            "spider": "max",
            "max_url": data["link"]
        }
        r = requests.post(url, data=payload)
        print data['link']
    return HttpResponse("Yo")

def data(request):
    schools = collection.find().distinct("school")
    players = {"data": {}}
    for school in schools:
        players["data"][school] = {
            "Passing": [],
            "Receiving": [],
            "Rushing": []
        }
    print players
    # school_one = collection.find({"school": schools[0]}).sort("category", ASCENDING)
    all_data = collection.find().sort("category", ASCENDING)
    for player in all_data:
        if player["category"] == "Passing":
            # print "passer"
            players['data'][player["school"]]["Passing"].append(player)
        elif player["category"] == "Receiving":
            # print "receiver"
            players['data'][player["school"]]["Receiving"].append(player)
        elif player["category"] == "Rushing":
            # print "rusher"
            players['data'][player["school"]]["Rushing"].append(player)
    print players

    return render(request, "data.html", players)