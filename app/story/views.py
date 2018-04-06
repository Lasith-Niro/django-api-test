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
    sele_story = Story.objects.filter(id=story_id)
    data = serializers.serialize('json', sele_story)
    return HttpResponse(data, content_type='application/json')
    
def getRatings(requests, story_id):
    sele_story = Story.objects.filter(id=story_id).values('rating') #.only('rating')
    return JsonResponse({'results':list(sele_story)})
    