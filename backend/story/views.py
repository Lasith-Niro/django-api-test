from django.shortcuts import render
from django.conf import settings
import requests
from tastypie.resources import ModelResource
from story.models import Story
from django.http import JsonResponse
from django.http import HttpResponse

import json
# serializing outputs
from django.core import serializers

def home(request):
    stories = Story.objects.order_by('-created_at')[:5]
    data = serializers.serialize('json', stories)
    return HttpResponse(data, content_type='application/json')

def getOne(requests, story_id):
    # stid = requests.GET['story_id']
    thisStory = Story.objects.filter(id=story_id)
    data = serializers.serialize('json', thisStory)
    return HttpResponse(data, content_type='application/json')
    
def getRatings(requests, story_id):
    thisStory = Story.objects.filter(id=story_id).values('rating') #.only('rating')
    return JsonResponse({'results':list(thisStory)})

def updateRatings(requests, story_id, rate):
    thisStory = Story.objects.get(id=story_id)
    thisStory.rating=rate
    thisStory.save()
    return JsonResponse({'code':1})

def updateTest(requests, data):
    if requests.method=='POST':
        print(data)
        return JsonResponse({'code':1, 'data':data})