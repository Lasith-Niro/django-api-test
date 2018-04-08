from tastypie.resources import ModelResource
from story.models import Story

class StoryResource(ModelResource):
    class Meta:
        queryset = Story.objects.order_by('-created_at')[:5]
        resource_name = 'stories'

class OneStory(ModelResource):
    def getOne(request, story_id=None):
        stid=request.GET.get('story_id')
        queryset = Story.objects.filter(id=stid)
        resource_name='story'

    
    # class Meta:

#         stid = Story.objects.get(story_id=story_id)

