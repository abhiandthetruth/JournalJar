from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'jar/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'jar/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    print(topic)
    #minus for reverse order
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'jar/topic.html', context)
